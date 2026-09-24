"""Unit tests for augproxy's policy and CONNECT handling. No network: resolver and connector
are injected, and the handler runs over socketpairs."""
import json
import socket
import threading
import unittest

import augproxy as ap

EXACT, SUFFIXES = ap.load_allowlist(["pypi.org", "files.pythonhosted.org  # wheels",
                                     "huggingface.co", "*.xethub.hf.co", ""])
PUBLIC = "151.101.0.223"


def resolver_for(mapping):
    def resolve(host, port):
        if host not in mapping:
            raise socket.gaierror("no such host")
        return mapping[host]
    return resolve


GOOD = resolver_for({"pypi.org": [PUBLIC], "files.pythonhosted.org": [PUBLIC],
                     "huggingface.co": ["2600:9000:2450::1", PUBLIC],
                     "cas-bridge.xethub.hf.co": [PUBLIC]})


def d(target, resolver=GOOD):
    return ap.decide(target, EXACT, SUFFIXES, resolver)


class Policy(unittest.TestCase):
    def test_named_host_allowed(self):
        r = d("pypi.org:443")
        self.assertTrue(r.allow)
        self.assertEqual((r.host, r.address), ("pypi.org", PUBLIC))

    def test_case_and_trailing_dot_normalized(self):
        self.assertTrue(d("PyPI.Org.:443").allow)

    def test_suffix_entry_covers_subdomains_only(self):
        self.assertTrue(d("cas-bridge.xethub.hf.co:443").allow)
        self.assertEqual(d("xethub.hf.co:443").reason, "not_allowlisted")
        self.assertEqual(d("evilxethub.hf.co:443").reason, "not_allowlisted")

    def test_unlisted_host_refused(self):
        self.assertEqual(d("example.com:443").reason, "not_allowlisted")
        self.assertEqual(d("pypi.org.evil.com:443").reason, "not_allowlisted")

    def test_typesafe_variants_denied(self):
        for t in ["typesafe.ai:443", "TYPESAFE.AI:443", "typesafe.ai.:443", "docs.typesafe.ai:443",
                  "a.b.typesafe.ai:443", "ｔｙｐｅｓａｆｅ.ai:443"]:
            with self.subTest(t=t):
                self.assertEqual(d(t).reason, "denied_suffix")

    def test_lookalikes_are_not_the_denied_domain(self):
        # Not typesafe.ai, and not allowlisted either.
        self.assertEqual(d("nottypesafe.ai:443").reason, "not_allowlisted")
        self.assertEqual(d("typesafe.ai.example.com:443").reason, "not_allowlisted")

    def test_deny_wins_over_allowlist(self):
        exact, suffixes = ap.load_allowlist(["*.ai"])
        r = ap.decide("docs.typesafe.ai:443", exact, suffixes, resolver_for({"docs.typesafe.ai": [PUBLIC]}))
        self.assertEqual(r.reason, "denied_suffix")

    def test_main_refuses_allowlist_naming_denied_host(self):
        import os, tempfile
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".txt") as f:
            f.write("typesafe.ai\n")
        try:
            with self.assertRaises(SystemExit):
                ap.main(["--allowlist", f.name, "--port", "0"])
        finally:
            os.unlink(f.name)

    def test_ip_literals_refused(self):
        for t in ["1.2.3.4:443", "127.0.0.1:443", "[::1]:443", "[2606:4700::1]:443", "2130706433:443",
                  "0x7f000001:443", "127.1:443", "0177.0.0.1:443", "10.0.0.1.:443"]:
            with self.subTest(t=t):
                self.assertEqual(d(t).reason, "ip_literal")

    def test_ports_other_than_443_refused(self):
        for t in ["pypi.org:80", "pypi.org:4430", "pypi.org:0443x", "pypi.org:22"]:
            with self.subTest(t=t):
                self.assertFalse(d(t).allow)
        self.assertEqual(d("pypi.org:80").reason, "port_not_443")

    def test_malformed_targets_refused(self):
        for t in ["pypi.org", ":443", "", "pypi..org:443", "-bad.org:443", "a" * 300 + ".org:443",
                  "pypi.org:443:443", "py pi.org:443", "pypi_org.org:443"]:
            with self.subTest(t=t):
                self.assertFalse(d(t).allow)

    def test_non_public_resolution_refused(self):
        for addrs in (["127.0.0.1"], ["10.1.2.3"], ["100.76.84.16"], ["169.254.1.1"],
                      ["192.168.1.210"], ["::1"], ["fe80::1"], ["fd7a:115c:a1e0::1"],
                      ["::ffff:127.0.0.1"], [PUBLIC, "10.42.0.5"], ["224.0.0.1"]):
            with self.subTest(addrs=addrs):
                r = d("pypi.org:443", resolver_for({"pypi.org": addrs}))
                self.assertEqual(r.reason, "non_public_address")

    def test_resolution_failure_refused(self):
        self.assertTrue(d("pypi.org:443", resolver_for({})).reason.startswith("resolve_failed"))
        self.assertEqual(d("pypi.org:443", resolver_for({"pypi.org": []})).reason, "resolve_empty")

    def test_first_address_is_the_one_connected(self):
        r = d("huggingface.co:443")
        self.assertEqual(r.address, "2600:9000:2450::1")


def client_hello(server_hostname):
    """A real ClientHello from the stdlib TLS stack, captured from a memory BIO."""
    import ssl
    ctx = ssl.create_default_context()
    if server_hostname is None:
        ctx.check_hostname = False
    inc, out = ssl.MemoryBIO(), ssl.MemoryBIO()
    obj = ctx.wrap_bio(inc, out, server_hostname=server_hostname)
    try:
        obj.do_handshake()
    except ssl.SSLWantReadError:
        pass
    return out.read()


def refragment(hello: bytes, cut: int) -> bytes:
    """Split one handshake record into two records at byte ``cut`` of its body."""
    body = hello[5:5 + int.from_bytes(hello[3:5], "big")]
    head = hello[:3]
    a, b = body[:cut], body[cut:]
    return head + len(a).to_bytes(2, "big") + a + head + len(b).to_bytes(2, "big") + b


class Hello(unittest.TestCase):
    def test_real_client_hello_sni(self):
        h = client_hello("pypi.org")
        self.assertEqual(ap.client_hello_sni(h), ("pypi.org", len(h)))

    def test_no_sni(self):
        self.assertEqual(ap.client_hello_sni(client_hello(None))[0], None)

    def test_partial_needs_more(self):
        h = client_hello("pypi.org")
        for n in (0, 3, 5, len(h) - 1):
            with self.subTest(n=n), self.assertRaises(IndexError):
                ap.client_hello_sni(h[:n])

    def test_fragmented_across_records(self):
        h = client_hello("files.pythonhosted.org")
        self.assertEqual(ap.client_hello_sni(refragment(h, 40))[0], "files.pythonhosted.org")

    def test_not_tls(self):
        for junk in (b"GET / HTTP/1.1\r\n\r\n", b"\x17\x03\x03\x00\x05hello", b"\x16\x02\x00\x00\x01x"):
            with self.subTest(junk=junk), self.assertRaises(ap.HelloError):
                ap.client_hello_sni(junk)

    def test_truncated_body_is_not_need_more(self):
        # A complete handshake header claiming a tiny body must be an error, not a wait.
        rec = b"\x16\x03\x01\x00\x08" + b"\x01\x00\x00\x04" + b"\x03\x03\x00\x00"
        with self.assertRaises(ap.HelloError):
            ap.client_hello_sni(rec)


def patch_sni(hello: bytes, list_delta=0, name_delta=0) -> bytes:
    """Corrupt the SNI extension's list or name length in place."""
    i = hello.find(b"\x00\x00", 5 + 4 + 2 + 32)
    while True:
        elen = int.from_bytes(hello[i + 2:i + 4], "big")
        data = hello[i + 4:i + 4 + elen]
        if len(data) >= 5 and data[2] == 0 and 2 + int.from_bytes(data[0:2], "big") == len(data):
            break
        i = hello.find(b"\x00\x00", i + 1)
    b = bytearray(hello)
    lst = int.from_bytes(b[i + 4:i + 6], "big") + list_delta
    b[i + 4:i + 6] = lst.to_bytes(2, "big")
    nl = int.from_bytes(b[i + 7:i + 9], "big") + name_delta
    b[i + 7:i + 9] = nl.to_bytes(2, "big")
    return bytes(b)


class HelloLengths(unittest.TestCase):
    def test_bad_list_length_refused(self):
        with self.assertRaises(ap.HelloError):
            ap.client_hello_sni(patch_sni(client_hello("pypi.org"), list_delta=5))

    def test_name_overrun_refused(self):
        with self.assertRaises(ap.HelloError):
            ap.client_hello_sni(patch_sni(client_hello("pypi.org"), name_delta=92))


class Serve(unittest.TestCase):
    def test_serve_accepts_and_refuses_over_real_socket(self):
        logs = []
        proxy = ap.Proxy(EXACT, SUFFIXES, logs.append, GOOD, lambda addr: (_ for _ in ()).throw(OSError()))
        self.assertTrue(hasattr(proxy, "slots"))
        probe = socket.socket(); probe.bind(("127.0.0.1", 0)); port = probe.getsockname()[1]; probe.close()
        t = threading.Thread(target=proxy.serve, args=("127.0.0.1", port), daemon=True)
        t.start()
        import time as _time
        for _ in range(100):
            try:
                c = socket.create_connection(("127.0.0.1", port), 1)
                break
            except OSError:
                _time.sleep(0.02)
        c.sendall(b"CONNECT example.com:443 HTTP/1.1\r\n\r\n")
        c.settimeout(5)
        self.assertTrue(c.recv(1024).startswith(b"HTTP/1.1 403"))
        c.close()
        for _ in range(100):
            if any('"not_allowlisted"' in l for l in logs):
                break
            _time.sleep(0.02)
        self.assertTrue(t.is_alive())
        self.assertTrue(any('"not_allowlisted"' in l for l in logs))


class Handler(unittest.TestCase):
    """Drive Proxy.handle over a socketpair with an injected upstream."""

    def run_request(self, raw: bytes, upstream_reply: bytes = b"", resolver=GOOD, close_after=False):
        logs, connected = [], []
        up_client, up_server = socket.socketpair()

        def connector(addr):
            connected.append(addr)
            return up_client

        proxy = ap.Proxy(EXACT, SUFFIXES, logs.append, resolver, connector)
        client, server_side = socket.socketpair()
        t = threading.Thread(target=proxy.handle, args=(server_side, ("127.0.0.1", 5555)))
        t.start()
        client.sendall(raw)
        if close_after:
            client.shutdown(socket.SHUT_WR)
        client.settimeout(5)
        response = b""
        try:
            while b"\r\n\r\n" not in response:
                chunk = client.recv(1024)
                if not chunk:
                    break
                response += chunk
        except socket.timeout:
            pass
        tunneled = b""
        import time as _time
        waited = _time.monotonic() + 5
        while response.startswith(b"HTTP/1.1 200") and not connected and t.is_alive() \
                and _time.monotonic() < waited:
            _time.sleep(0.01)
        if response.startswith(b"HTTP/1.1 200") and connected:
            up_server.settimeout(5)
            tunneled = up_server.recv(1024)
            up_server.sendall(upstream_reply)
            got = client.recv(1024)
            self.assertEqual(got, upstream_reply)
            up_server.close()
        client.close()
        t.join(5)
        up_server.close()
        if not connected:
            up_client.close()
        return response, [json.loads(line) for line in logs], connected, tunneled

    def test_allowed_connect_tunnels_bytes(self):
        hello = client_hello("pypi.org")
        resp, logs, connected, tunneled = self.run_request(
            b"CONNECT pypi.org:443 HTTP/1.1\r\nHost: pypi.org:443\r\n\r\n" + hello, b"WORLD")
        self.assertTrue(resp.startswith(b"HTTP/1.1 200"))
        self.assertEqual(connected, [PUBLIC])
        self.assertEqual(tunneled, hello[:1024])
        self.assertEqual(logs[-1]["verdict"], "allow")

    def test_sni_mismatch_never_connects(self):
        for sni in ("anything.github.io", "docs.typesafe.ai", None):
            with self.subTest(sni=sni):
                resp, logs, connected, _ = self.run_request(
                    b"CONNECT pypi.org:443 HTTP/1.1\r\n\r\n" + client_hello(sni))
                self.assertEqual(connected, [])
                self.assertEqual(logs[-1]["reason"], "sni_mismatch")

    def test_non_tls_tunnel_never_connects(self):
        resp, logs, connected, _ = self.run_request(
            b"CONNECT pypi.org:443 HTTP/1.1\r\n\r\nGET / HTTP/1.1\r\nHost: x\r\n\r\n")
        self.assertEqual(connected, [])
        self.assertEqual(logs[-1]["reason"], "not_tls_client_hello")

    def test_client_closing_before_hello_never_connects(self):
        resp, logs, connected, _ = self.run_request(b"CONNECT pypi.org:443 HTTP/1.1\r\n\r\n",
                                                    close_after=True)
        self.assertEqual(connected, [])
        self.assertEqual(logs[-1]["reason"], "sni_missing")

    def test_falls_back_to_next_vetted_address(self):
        logs, tried = [], []
        up_client, up_server = socket.socketpair()

        def connector(addr):
            tried.append(addr)
            if addr != PUBLIC:
                raise OSError("no route")
            return up_client

        proxy = ap.Proxy(EXACT, SUFFIXES, logs.append, GOOD, connector)
        client, server_side = socket.socketpair()
        t = threading.Thread(target=proxy.handle, args=(server_side, ("127.0.0.1", 1)))
        t.start()
        client.sendall(b"CONNECT huggingface.co:443 HTTP/1.1\r\n\r\n" + client_hello("huggingface.co"))
        client.settimeout(5)
        client.recv(1024)
        up_server.settimeout(5)
        self.assertTrue(up_server.recv(5).startswith(b"\x16\x03"))
        up_server.close(); client.close(); t.join(5)
        self.assertEqual(tried, ["2600:9000:2450::1", PUBLIC])
        self.assertEqual(json.loads(logs[-1])["address"], PUBLIC)

    def test_refused_connect_logs_and_never_connects(self):
        resp, logs, connected, _ = self.run_request(b"CONNECT typesafe.ai:443 HTTP/1.1\r\n\r\n")
        self.assertTrue(resp.startswith(b"HTTP/1.1 403"))
        self.assertEqual(connected, [])
        self.assertEqual((logs[-1]["verdict"], logs[-1]["reason"]), ("deny", "denied_suffix"))

    def test_plain_http_refused(self):
        resp, logs, connected, _ = self.run_request(b"GET http://pypi.org/ HTTP/1.1\r\n\r\n")
        self.assertTrue(resp.startswith(b"HTTP/1.1 405"))
        self.assertEqual(connected, [])
        self.assertEqual(logs[-1]["reason"], "method_not_connect")

    def test_bad_request_line_refused(self):
        resp, logs, _, _ = self.run_request(b"CONNECT pypi.org:443\r\n\r\n")
        self.assertTrue(resp.startswith(b"HTTP/1.1 400"))

    def test_oversized_header_refused(self):
        resp, logs, connected, _ = self.run_request(b"CONNECT pypi.org:443 HTTP/1.1\r\nX: " + b"a" * 9000)
        self.assertTrue(resp.startswith(b"HTTP/1.1 431"))
        self.assertEqual(connected, [])

    def test_connect_failure_is_logged_and_closed(self):
        logs = []

        def failing(addr):
            raise ConnectionRefusedError()

        proxy = ap.Proxy(EXACT, SUFFIXES, logs.append, GOOD, failing)
        client, server_side = socket.socketpair()
        t = threading.Thread(target=proxy.handle, args=(server_side, ("127.0.0.1", 1)))
        t.start()
        client.sendall(b"CONNECT pypi.org:443 HTTP/1.1\r\n\r\n" + client_hello("pypi.org"))
        client.settimeout(5)
        self.assertTrue(client.recv(1024).startswith(b"HTTP/1.1 200"))
        t.join(5)
        client.close()
        self.assertTrue(json.loads(logs[-1])["reason"].startswith("connect_failed"))

    def test_serve_refuses_non_loopback_bind(self):
        with self.assertRaises(SystemExit):
            ap.Proxy(EXACT, SUFFIXES, print).serve("0.0.0.0", 0)


if __name__ == "__main__":
    unittest.main()
