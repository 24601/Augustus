#!/usr/bin/env python3
"""A minimal stdlib Parquet reader: enough to normalize a corpus, nothing more.

This exists as a fallback. If `augctl` can get pyarrow through the proxy
window, use pyarrow: it is better tested than this, and this file should then
never run. But augctl is the only principal allowed to see confirmation labels,
it may not run containers, and no install is permitted outside a window, so a
missing wheel must not be able to block the whole experiment.

Scope, deliberately narrow:
  * Parquet 1.0/2.x files whose columns are BYTE_ARRAY (UTF8), BOOLEAN,
    INT32/64, FLOAT/DOUBLE;
  * PLAIN and RLE_DICTIONARY encodings, which is what the Hub's converted
    corpora use;
  * UNCOMPRESSED, SNAPPY and GZIP page compression;
  * required and optional columns at the top level, with definition levels
    read only well enough to place nulls.

It refuses anything outside that rather than guessing, because a silently
misread column would corrupt a label and no downstream check would catch it.
Nested and repeated fields are refused outright.
"""

from __future__ import annotations

import gzip
import struct
from dataclasses import dataclass


class ParquetUnsupported(Exception):
    """A construct this reader will not guess at."""


MAGIC = b"PAR1"

# Thrift compact protocol, the subset the Parquet metadata uses.
T_STOP, T_TRUE, T_FALSE, T_I8, T_I16, T_I32, T_I64 = 0, 1, 2, 3, 4, 5, 6
T_DOUBLE, T_BINARY, T_LIST, T_SET, T_MAP, T_STRUCT = 7, 8, 9, 10, 11, 12


class Thrift:
    """Just enough compact-protocol decoding to walk Parquet's FileMetaData."""

    def __init__(self, data: bytes, offset: int = 0):
        self.data = data
        self.pos = offset

    def byte(self) -> int:
        value = self.data[self.pos]
        self.pos += 1
        return value

    def varint(self) -> int:
        result = 0
        shift = 0
        while True:
            byte = self.byte()
            result |= (byte & 0x7F) << shift
            if not byte & 0x80:
                return result
            shift += 7

    def zigzag(self) -> int:
        value = self.varint()
        return (value >> 1) ^ -(value & 1)

    def binary(self) -> bytes:
        length = self.varint()
        out = self.data[self.pos:self.pos + length]
        self.pos += length
        return out

    def struct(self) -> dict:
        """Returns {field_id: value}. Unknown types raise rather than skip."""
        fields = {}
        last_id = 0
        while True:
            header = self.byte()
            if header == T_STOP:
                return fields
            delta, type_id = header >> 4, header & 0x0F
            field_id = last_id + delta if delta else self.zigzag()
            last_id = field_id
            fields[field_id] = self.value(type_id)

    def value(self, type_id: int):
        if type_id == T_TRUE:
            return True
        if type_id == T_FALSE:
            return False
        if type_id in (T_I8,):
            return self.byte()
        if type_id in (T_I16, T_I32, T_I64):
            return self.zigzag()
        if type_id == T_DOUBLE:
            out = struct.unpack("<d", self.data[self.pos:self.pos + 8])[0]
            self.pos += 8
            return out
        if type_id == T_BINARY:
            return self.binary()
        if type_id == T_STRUCT:
            return self.struct()
        if type_id in (T_LIST, T_SET):
            header = self.byte()
            size, element = header >> 4, header & 0x0F
            if size == 15:
                size = self.varint()
            return [self.value(element) for _ in range(size)]
        if type_id == T_MAP:
            size = self.varint()
            if size == 0:
                return {}
            kinds = self.byte()
            key_type, value_type = kinds >> 4, kinds & 0x0F
            return {self.value(key_type): self.value(value_type) for _ in range(size)}
        raise ParquetUnsupported(f"thrift type {type_id}")


# Parquet enums, by the values in parquet.thrift.
PHYSICAL = {0: "BOOLEAN", 1: "INT32", 2: "INT64", 3: "INT96", 4: "FLOAT",
            5: "DOUBLE", 6: "BYTE_ARRAY", 7: "FIXED_LEN_BYTE_ARRAY"}
ENCODING = {0: "PLAIN", 2: "PLAIN_DICTIONARY", 3: "RLE", 4: "BIT_PACKED",
            8: "RLE_DICTIONARY"}
COMPRESSION = {0: "UNCOMPRESSED", 1: "SNAPPY", 2: "GZIP", 3: "LZO",
               4: "BROTLI", 5: "LZ4", 6: "ZSTD"}
SUPPORTED_PHYSICAL = {"BOOLEAN", "INT32", "INT64", "FLOAT", "DOUBLE", "BYTE_ARRAY"}


@dataclass
class Column:
    name: str
    physical: str
    optional: bool


def read_footer(data: bytes) -> dict:
    if data[:4] != MAGIC or data[-4:] != MAGIC:
        raise ParquetUnsupported("not a parquet file: missing PAR1 magic")
    length = struct.unpack("<I", data[-8:-4])[0]
    start = len(data) - 8 - length
    return Thrift(data, start).struct()


def schema_columns(footer: dict) -> list[Column]:
    """Top-level leaf columns only. A nested or repeated field is refused."""
    elements = footer.get(2) or []
    columns = []
    for element in elements[1:]:
        num_children = element.get(5)
        if num_children:
            raise ParquetUnsupported("nested schema: this reader handles flat columns only")
        repetition = element.get(3, 0)  # 0 REQUIRED, 1 OPTIONAL, 2 REPEATED
        if repetition == 2:
            raise ParquetUnsupported("repeated field: this reader handles flat columns only")
        physical = PHYSICAL.get(element.get(1))
        if physical not in SUPPORTED_PHYSICAL:
            raise ParquetUnsupported(f"physical type {physical}")
        name = element.get(4)
        columns.append(Column(name.decode("utf-8") if isinstance(name, bytes) else str(name),
                              physical, repetition == 1))
    return columns


def snappy_raw_decompress(data: bytes) -> bytes:
    """Snappy raw block format. Written out because there is no stdlib snappy.

    Format: a varint of the uncompressed length, then tagged elements that are
    either literals or back-references into the output produced so far.
    """
    pos = 0
    shift = 0
    expected = 0
    while True:
        byte = data[pos]
        pos += 1
        expected |= (byte & 0x7F) << shift
        if not byte & 0x80:
            break
        shift += 7

    out = bytearray()
    while pos < len(data):
        tag = data[pos]
        pos += 1
        kind = tag & 0x03
        if kind == 0:  # literal
            length = tag >> 2
            if length < 60:
                length += 1
            else:
                extra = length - 59
                length = int.from_bytes(data[pos:pos + extra], "little") + 1
                pos += extra
            out += data[pos:pos + length]
            pos += length
            continue
        if kind == 1:  # copy with a 1-byte offset
            length = 4 + ((tag >> 2) & 0x07)
            offset = ((tag >> 5) << 8) | data[pos]
            pos += 1
        elif kind == 2:  # copy with a 2-byte offset
            length = (tag >> 2) + 1
            offset = int.from_bytes(data[pos:pos + 2], "little")
            pos += 2
        else:  # copy with a 4-byte offset
            length = (tag >> 2) + 1
            offset = int.from_bytes(data[pos:pos + 4], "little")
            pos += 4
        if offset <= 0 or offset > len(out):
            raise ParquetUnsupported("snappy: offset outside the output window")
        start = len(out) - offset
        for i in range(length):  # may overlap, so copy byte by byte
            out.append(out[start + i])
    if len(out) != expected:
        raise ParquetUnsupported(
            f"snappy: decompressed {len(out)} bytes, header said {expected}")
    return bytes(out)


def decompress(payload: bytes, codec: int, uncompressed_size: int) -> bytes:
    name = COMPRESSION.get(codec)
    if name == "UNCOMPRESSED":
        return payload
    if name == "GZIP":
        return gzip.decompress(payload)
    if name == "SNAPPY":
        return snappy_raw_decompress(payload)
    raise ParquetUnsupported(f"compression {name or codec}")


def bit_width(max_value: int) -> int:
    return max_value.bit_length()


def read_rle_bit_packed(data: bytes, width: int, count: int) -> list[int]:
    """The hybrid RLE / bit-packed run encoding, used for levels and dict indices."""
    values: list[int] = []
    pos = 0
    while len(values) < count and pos < len(data):
        header = 0
        shift = 0
        while True:
            byte = data[pos]
            pos += 1
            header |= (byte & 0x7F) << shift
            if not byte & 0x80:
                break
            shift += 7
        if header & 1:  # bit-packed run: (header >> 1) groups of 8
            groups = header >> 1
            total_bits = groups * 8 * width
            chunk = data[pos:pos + (total_bits + 7) // 8]
            pos += len(chunk)
            acc = int.from_bytes(chunk, "little")
            for i in range(groups * 8):
                if len(values) >= count:
                    break
                values.append((acc >> (i * width)) & ((1 << width) - 1))
        else:  # RLE run: (header >> 1) repeats of one value
            repeats = header >> 1
            size = (width + 7) // 8
            value = int.from_bytes(data[pos:pos + size], "little")
            pos += size
            values.extend([value] * min(repeats, count - len(values)))
    return values


def decode_plain(data: bytes, physical: str, count: int) -> list:
    out = []
    pos = 0
    for _ in range(count):
        if physical == "BYTE_ARRAY":
            length = struct.unpack("<I", data[pos:pos + 4])[0]
            pos += 4
            out.append(data[pos:pos + length].decode("utf-8", "replace"))
            pos += length
        elif physical == "INT32":
            out.append(struct.unpack("<i", data[pos:pos + 4])[0]); pos += 4
        elif physical == "INT64":
            out.append(struct.unpack("<q", data[pos:pos + 8])[0]); pos += 8
        elif physical == "FLOAT":
            out.append(struct.unpack("<f", data[pos:pos + 4])[0]); pos += 4
        elif physical == "DOUBLE":
            out.append(struct.unpack("<d", data[pos:pos + 8])[0]); pos += 8
        elif physical == "BOOLEAN":
            # PLAIN booleans are bit-packed, one bit per value, LSB first.
            index = len(out)
            out.append(bool((data[index // 8] >> (index % 8)) & 1))
        else:
            raise ParquetUnsupported(physical)
    return out


def read_column_chunk(data: bytes, chunk_meta: dict, column: Column) -> list:
    """Every value in one column chunk, with None for nulls."""
    # ColumnMetaData field ids, from parquet.thrift: 4 codec, 5 num_values,
    # 9 data_page_offset, 11 dictionary_page_offset. Field 2 is `encodings`,
    # a list, which is what an earlier draft read as the offset.
    codec = chunk_meta.get(4, 0)
    offset = chunk_meta.get(9)
    dict_offset = chunk_meta.get(11)
    start = min(offset, dict_offset) if dict_offset else offset
    total_values = chunk_meta.get(5, 0)

    values: list = []
    dictionary: list = []
    pos = start
    while len(values) < total_values:
        header_reader = Thrift(data, pos)
        header = header_reader.struct()
        pos = header_reader.pos
        page_type = header.get(1)          # 0 DATA_PAGE, 1 INDEX, 2 DICTIONARY, 3 DATA_PAGE_V2
        uncompressed = header.get(2)
        compressed = header.get(3)
        payload = decompress(data[pos:pos + compressed], codec, uncompressed)
        pos += compressed

        if page_type == 2:  # dictionary page
            meta = header.get(7, {})
            dictionary = decode_plain(payload, column.physical, meta.get(1, 0))
            continue
        if page_type == 0:  # data page v1
            meta = header.get(5, {})
            count = meta.get(1, 0)
            encoding = ENCODING.get(meta.get(2))
            definitions = None
            body = payload
            if column.optional:
                length = struct.unpack("<I", body[:4])[0]
                definitions = read_rle_bit_packed(body[4:4 + length], 1, count)
                body = body[4 + length:]
            present = count if definitions is None else sum(definitions)
            if encoding == "PLAIN":
                decoded = decode_plain(body, column.physical, present)
            elif encoding in ("RLE_DICTIONARY", "PLAIN_DICTIONARY"):
                width = body[0]
                indices = read_rle_bit_packed(body[1:], width, present)
                decoded = [dictionary[i] for i in indices]
            else:
                raise ParquetUnsupported(f"encoding {encoding}")
            if definitions is None:
                values.extend(decoded)
            else:
                iterator = iter(decoded)
                values.extend(next(iterator) if d else None for d in definitions)
            continue
        raise ParquetUnsupported(f"page type {page_type}; only v1 data and dictionary pages")
    return values[:total_values]


def read_table(path, columns: list[str] | None = None) -> dict[str, list]:
    """Read a whole flat Parquet file into {column: values}.

    Reads the file into memory: the corpora this is for are a few GB at most,
    and the host has 100 GiB free. Streaming would be better and is not needed.
    """
    with open(path, "rb") as handle:
        data = handle.read()
    footer = read_footer(data)
    schema = schema_columns(footer)
    wanted = {c.name for c in schema} if columns is None else set(columns)
    missing = wanted - {c.name for c in schema}
    if missing:
        raise ParquetUnsupported(f"no such column: {sorted(missing)}")

    out: dict[str, list] = {name: [] for name in wanted}
    for row_group in footer.get(4) or []:
        for chunk in row_group.get(1) or []:
            meta = chunk.get(3) or {}
            path_in_schema = meta.get(3) or []
            name = path_in_schema[0].decode() if path_in_schema else None
            if name not in wanted:
                continue
            column = next(c for c in schema if c.name == name)
            out[name].extend(read_column_chunk(data, meta, column))
    return out
