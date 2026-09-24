#!/usr/bin/env python3
"""Augustus 0.8.0 setup proxy: a stdlib HTTPS CONNECT proxy with a named-host allowlist.

Runs as the unprivileged ``augproxy`` user on tabputer-1, bound to 127.0.0.1 only, and only
while a setup window is open. The nftables table ``inet augexp`` lets ``augexp`` reach nothing
but this port, and lets ``augproxy`` reach only the resolved stub and public TCP 443.

Policy, in order:
1. Only ``CONNECT host:443``. Other methods, ports and malformed requests are refused.
2. The host must be a DNS name. IP literals in any spelling are refused, including dotted,
   integer, hex and short forms, and bracketed IPv6.
3. The name is normalized: lowercase, one trailing dot dropped, IDNA to ASCII. It is then
   checked against the deny suffixes (``typesafe.ai`` and every subdomain) before the
   allowlist. A deny always wins.
4. The name must be on the allowlist. Entries are exact names, or ``*.suffix`` for
   subdomains of a suffix.
5. Every resolved address must be globally routable. One non-global address refuses the
   request (rebinding defense). The proxy connects only to the vetted addresses, in order, and
   never resolves again.
6. The tunnel's first bytes must be a TLS ClientHello whose server_name equals the CONNECT
   host. On a shared CDN edge, an allowlisted CONNECT would otherwise reach any tenant.
   Tunnel contents after the ClientHello are not inspected, so domain fronting through a CDN
   that permits it is out of scope (see plan §4.6).

Every decision is logged as one JSON line.
"""
from __future__ import annotations

import argparse
import ipaddress
import json
import re
import socket
import sys
import threading
import time
from dataclasses import dataclass
from typing import Callable, Iterable, Sequence

DENY_SUFFIXES = ("typesafe.ai",)
MAX_HEADER = 8192
HEADER_TIMEOUT = 10.0
CONNECT_TIMEOUT = 15.0
IDLE_TIMEOUT = 300.0
MAX_CLIENTS = 64
MAX_HELLO = 65536

_LABEL = re.compile(r"^(?!-)[a-z0-9-]{1,63}(?<!-)$")
_NUMERICISH = re.compile(r"^(0x[0-9a-f]+|[0-9]+)$")


@dataclass(frozen=True)
class Decision:
    allow: bool
    reason: str
    host: str = ""
    address: str = ""
    addresses: tuple = ()


def normalize_host(raw: str) -> str:
    """Lowercase, drop one trailing dot, IDNA-encode. Raises ValueError on a malformed name."""
    host = raw.strip()
    if not host or len(host) > 253 + 1:
        raise ValueError("empty or overlong host")
    if host.endswith("."):
        host = host[:-1]
    if not host or host.endswith("."):
        raise ValueError("empty label")
    try:
        ascii_host = host.encode("idna").decode("ascii").lower()
    except UnicodeError as exc:
        raise ValueError(f"idna: {exc}") from None
    labels = ascii_host.split(".")
    if any(not _LABEL.match(label) for label in labels):
        raise ValueError("invalid label")
    return ascii_host


def is_ip_literal(host: str) -> bool:
    """True for anything a resolver could read as an address rather than a name."""
    h = host.strip("[]").rstrip(".").lower()
    try:
        ipaddress.ip_address(h)
        return True
    except ValueError:
        pass
    # inet_aton accepts 127.1, 2130706433, 0x7f.1 and friends; refuse every all-numeric shape.
    parts = h.split(".")
    if parts and all(_NUMERICISH.match(p) for p in parts if p):
        return True
    # A name whose last label is numeric is not a valid public hostname either.
    return bool(parts) and _NUMERICISH.match(parts[-1] or "x") is not None


def is_denied(host: str) -> bool:
    return any(host == s or host.endswith("." + s) for s in DENY_SUFFIXES)


def load_allowlist(lines: Iterable[str]) -> tuple[frozenset[str], tuple[str, ...]]:
    exact, suffixes = set(), []
    for line in lines:
        entry = line.split("#", 1)[0].strip()
        if not entry:
            continue
        if entry.startswith("*."):
            suffixes.append(normalize_host(entry[2:]))
        else:
            exact.add(normalize_host(entry))
    return frozenset(exact), tuple(suffixes)


def is_allowlisted(host: str, exact: frozenset[str], suffixes: Sequence[str]) -> bool:
    return host in exact or any(host.endswith("." + s) for s in suffixes)


def address_is_public(addr: str) -> bool:
    ip = ipaddress.ip_address(addr.split("%", 1)[0])
    if isinstance(ip, ipaddress.IPv6Address) and ip.ipv4_mapped is not None:
        ip = ip.ipv4_mapped
    return ip.is_global and not ip.is_multicast


Resolver = Callable[[str, int], list[str]]


def system_resolver(host: str, port: int) -> list[str]:
    infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
    seen: list[str] = []
    for *_ignored, sockaddr in infos:
        if sockaddr[0] not in seen:
            seen.append(sockaddr[0])
    return seen


def decide(target: str, exact: frozenset[str], suffixes: Sequence[str],
           resolver: Resolver = system_resolver) -> Decision:
    """Decide one CONNECT target of the form ``host:port``."""
    if target.startswith("["):
        return Decision(False, "ip_literal", target)
    host_part, sep, port_part = target.rpartition(":")
    if not sep or not host_part or not port_part.isdigit():
        return Decision(False, "malformed_target", target)
    if port_part != "443":
        return Decision(False, "port_not_443", target)
    if is_ip_literal(host_part):
        return Decision(False, "ip_literal", host_part)
    try:
        host = normalize_host(host_part)
    except ValueError as exc:
        return Decision(False, f"malformed_host:{exc}", host_part)
    if is_ip_literal(host):
        return Decision(False, "ip_literal", host)
    if is_denied(host):
        return Decision(False, "denied_suffix", host)
    if not is_allowlisted(host, exact, suffixes):
        return Decision(False, "not_allowlisted", host)
    try:
        addrs = resolver(host, 443)
    except OSError as exc:
        return Decision(False, f"resolve_failed:{exc.__class__.__name__}", host)
    if not addrs:
        return Decision(False, "resolve_empty", host)
    try:
        if not all(address_is_public(a) for a in addrs):
            return Decision(False, "non_public_address", host, ",".join(addrs))
    except ValueError:
        return Decision(False, "bad_address", host, ",".join(addrs))
    return Decision(True, "allowed", host, addrs[0], tuple(addrs))


class HelloError(ValueError):
    pass


def client_hello_sni(buf: bytes) -> tuple[str | None, int]:
    """Parse a TLS ClientHello from the start of ``buf``.

    Returns (server_name or None, bytes consumed) once the whole handshake message is
    present. Raises HelloError when the bytes are not a TLS ClientHello, and
    ``IndexError`` when more bytes are needed.
    """
    hs, i = b"", 0
    while True:
        if len(buf) < i + 5:
            raise IndexError("need record header")
        ctype, major, length = buf[i], buf[i + 1], int.from_bytes(buf[i + 3:i + 5], "big")
        if ctype != 0x16 or major != 3 or length == 0 or length > 16384 + 2048:
            raise HelloError("not a TLS handshake record")
        if len(buf) < i + 5 + length:
            raise IndexError("need record body")
        hs += buf[i + 5:i + 5 + length]
        i += 5 + length
        if len(hs) >= 4:
            if hs[0] != 0x01:
                raise HelloError("first handshake message is not ClientHello")
            need = 4 + int.from_bytes(hs[1:4], "big")
            if need > MAX_HELLO:
                raise HelloError("ClientHello too large")
            if len(hs) >= need:
                break
    try:
        return _hello_body_sni(hs[4:need]), i
    except IndexError:
        raise HelloError("ClientHello truncated") from None


def _hello_body_sni(body: bytes) -> str | None:
    p = 2 + 32
    p += 1 + body[p]                                   # session id
    p += 2 + int.from_bytes(body[p:p + 2], "big")      # cipher suites
    p += 1 + body[p]                                   # compression methods
    if p + 2 > len(body):
        return None
    end = p + 2 + int.from_bytes(body[p:p + 2], "big")
    p += 2
    if end > len(body):
        raise HelloError("extensions overrun")
    names = []
    while p + 4 <= end:
        etype, elen = int.from_bytes(body[p:p + 2], "big"), int.from_bytes(body[p + 2:p + 4], "big")
        data = body[p + 4:p + 4 + elen]
        p += 4 + elen
        if etype != 0:
            continue
        if len(data) < 2 or 2 + int.from_bytes(data[0:2], "big") != len(data):
            raise HelloError("server_name list length mismatch")
        q = 2
        while q < len(data):
            if q + 3 > len(data):
                raise HelloError("server_name entry truncated")
            ntype, nlen = data[q], int.from_bytes(data[q + 1:q + 3], "big")
            if nlen == 0 or q + 3 + nlen > len(data):
                raise HelloError("server_name length overrun")
            if ntype == 0:
                names.append(data[q + 3:q + 3 + nlen].decode("ascii", "strict"))
            q += 3 + nlen
    if p != end:
        raise HelloError("extensions malformed")
    if len(names) > 1:
        raise HelloError("multiple server names")
    return names[0] if names else None


class Proxy:
    def __init__(self, exact, suffixes, log, resolver: Resolver = system_resolver,
                 connector=None):
        self.exact, self.suffixes, self.log = exact, suffixes, log
        self.resolver = resolver
        self.connector = connector or (lambda addr: socket.create_connection((addr, 443),
                                                                           CONNECT_TIMEOUT))
        self.slots = threading.BoundedSemaphore(MAX_CLIENTS)

    def connect_first(self, addresses):
        last = None
        for addr in addresses:
            try:
                return addr, self.connector(addr)
            except OSError as exc:
                last = exc
        raise last or OSError("no address")

    def record(self, **fields):
        fields["ts"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        self.log(json.dumps(fields, sort_keys=True))

    def handle(self, client: socket.socket, peer) -> None:
        try:
            client.settimeout(HEADER_TIMEOUT)
            head = b""
            while b"\r\n\r\n" not in head:
                try:
                    chunk = client.recv(1024)
                except socket.timeout:
                    self.record(peer=peer[0], verdict="deny", reason="header_timeout")
                    return
                if not chunk:
                    return
                head += chunk
                if len(head) > MAX_HEADER:
                    self.reply(client, 431, "Request Header Fields Too Large")
                    self.record(peer=peer[0], verdict="deny", reason="header_too_large")
                    return
            line = head.split(b"\r\n", 1)[0].decode("latin-1")
            parts = line.split(" ")
            if len(parts) != 3 or not parts[2].startswith("HTTP/1."):
                self.reply(client, 400, "Bad Request")
                self.record(peer=peer[0], verdict="deny", reason="bad_request_line")
                return
            method, target, _version = parts
            if method != "CONNECT":
                self.reply(client, 405, "Method Not Allowed")
                self.record(peer=peer[0], verdict="deny", reason="method_not_connect",
                            method=method[:16])
                return
            d = decide(target, self.exact, self.suffixes, self.resolver)
            if not d.allow:
                self.reply(client, 403, "Forbidden")
                self.record(peer=peer[0], verdict="deny", reason=d.reason, target=target[:300],
                            host=d.host[:300], address=d.address)
                return
            # Say yes to the CONNECT, then require a ClientHello for this host before any byte
            # reaches the upstream. Nothing is connected until the SNI matches.
            self.reply(client, 200, "Connection Established")
            buf = head.split(b"\r\n\r\n", 1)[1]
            deadline = time.monotonic() + HEADER_TIMEOUT
            while True:
                try:
                    sni, _used = client_hello_sni(buf)
                    break
                except IndexError:
                    if len(buf) > MAX_HELLO + 5 * 8 or time.monotonic() > deadline:
                        self.record(peer=peer[0], verdict="deny", reason="sni_timeout", host=d.host)
                        return
                    try:
                        chunk = client.recv(16384)
                    except socket.timeout:
                        chunk = b""
                    if not chunk:
                        self.record(peer=peer[0], verdict="deny", reason="sni_missing", host=d.host)
                        return
                    buf += chunk
                except (HelloError, UnicodeDecodeError) as exc:
                    self.record(peer=peer[0], verdict="deny", reason="not_tls_client_hello",
                                host=d.host, detail=str(exc)[:120])
                    return
            try:
                sni_norm = normalize_host(sni) if sni else ""
            except ValueError:
                sni_norm = ""
            if sni_norm != d.host:
                self.record(peer=peer[0], verdict="deny", reason="sni_mismatch", host=d.host,
                            sni=(sni or "")[:300])
                return
            try:
                address, upstream = self.connect_first(d.addresses or (d.address,))
            except OSError as exc:
                self.record(peer=peer[0], verdict="deny", reason=f"connect_failed:{exc.__class__.__name__}",
                            host=d.host, address=",".join(d.addresses))
                return
            self.record(peer=peer[0], verdict="allow", reason=d.reason, host=d.host, address=address)
            upstream.sendall(buf)
            self.relay(client, upstream)
        finally:
            try:
                client.close()
            except OSError:
                pass

    @staticmethod
    def reply(sock, code, text):
        try:
            sock.sendall(f"HTTP/1.1 {code} {text}\r\nContent-Length: 0\r\n\r\n".encode())
        except OSError:
            pass

    @staticmethod
    def relay(a: socket.socket, b: socket.socket) -> None:
        a.settimeout(IDLE_TIMEOUT)
        b.settimeout(IDLE_TIMEOUT)

        def pump(src, dst):
            try:
                while True:
                    data = src.recv(65536)
                    if not data:
                        break
                    dst.sendall(data)
            except OSError:
                pass
            finally:
                for s in (dst,):
                    try:
                        s.shutdown(socket.SHUT_WR)
                    except OSError:
                        pass

        t = threading.Thread(target=pump, args=(b, a), daemon=True)
        t.start()
        pump(a, b)
        t.join(IDLE_TIMEOUT)
        try:
            b.close()
        except OSError:
            pass

    def serve(self, host: str, port: int) -> None:
        if host not in ("127.0.0.1", "::1"):
            raise SystemExit("refusing to bind a non-loopback address")
        family = socket.AF_INET6 if ":" in host else socket.AF_INET
        with socket.socket(family, socket.SOCK_STREAM) as srv:
            srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            srv.bind((host, port))
            srv.listen(128)
            self.record(event="listening", bind=f"{host}:{port}", exact=sorted(self.exact),
                        suffixes=list(self.suffixes), deny=list(DENY_SUFFIXES))
            while True:
                client, peer = srv.accept()
                if not self.slots.acquire(blocking=False):
                    self.reply(client, 503, "Service Unavailable")
                    self.record(peer=peer[0], verdict="deny", reason="too_many_clients")
                    client.close()
                    continue

                def run(c=client, p=peer):
                    try:
                        self.handle(c, p)
                    finally:
                        self.slots.release()

                threading.Thread(target=run, daemon=True).start()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bind", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=3128)
    ap.add_argument("--allowlist", required=True)
    ap.add_argument("--log", help="append JSON lines here as well as stdout")
    args = ap.parse_args(argv)
    with open(args.allowlist) as f:
        exact, suffixes = load_allowlist(f)
    for name in list(exact) + list(suffixes):
        if is_denied(name):
            raise SystemExit(f"allowlist names a denied host: {name}")
    log_file = open(args.log, "a", buffering=1) if args.log else None
    lock = threading.Lock()

    def log(line: str) -> None:
        with lock:
            print(line, flush=True)
            if log_file:
                log_file.write(line + "\n")

    Proxy(exact, suffixes, log).serve(args.bind, args.port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
