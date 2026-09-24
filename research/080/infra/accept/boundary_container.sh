#!/bin/bash
# Plan v3 §4.3 container-side boundary tests B7, B10, B12 and B14 on tabputer-1. Run as root.
# Containers are launched inside augexp's own user manager (systemd-run --user), so every
# container process lives in user-48201.slice (B15). Prints one RESULT line per test.
set -uo pipefail
[[ $EUID -eq 0 ]] || { echo "run as root" >&2; exit 1; }
IMG=docker.io/vllm/vllm-openai-rocm@sha256:e5e47f6aaab675c252c381f0dac237b31b10d87bb74d092b07fb4065efd7f5a1
HARD="--rm --read-only --tmpfs /tmp --cap-drop=all --security-opt=no-new-privileges --pids-limit=512 --memory=16g --memory-swap=16g --ipc=private"
fails=0
say() { printf '%s %s %s\n' "$1" "$2" "$3"; [[ $1 == PASS ]] || fails=$((fails+1)); }
urun() {  # run a command as augexp inside its user manager; stdout+stderr captured
  sudo -n -u augexp XDG_RUNTIME_DIR=/run/user/48201 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/48201/bus \
    systemd-run --user --quiet --wait --pipe --collect -p TimeoutStopSec=30 -- "$@" 2>&1
}
py() { local net=$1; shift; urun podman run $HARD --network="$net" -v "$RUNA:/work" --entrypoint python3 "$IMG" -c "$@"; }

RUNA=/srv/aug/runs/bt-a-$(date +%s); RUNB=/srv/aug/runs/bt-b-$(date +%s)
install -d -o augexp -g augexp -m 700 "$RUNA" "$RUNB"

# B7 inside a container: only /work and /tmp are writable.
out=$(urun podman run $HARD --network=none -v /srv/aug/stage/models:/stage/models:ro -v "$RUNA:/work" --entrypoint sh "$IMG" -c '
for d in / /usr /etc /stage/models /opt; do touch "$d/.w" 2>/dev/null && echo "W:$d"; done
touch /work/.w && echo OKWORK; touch /tmp/.w && echo OKTMP')
if grep -q '^W:' <<<"$out" || ! grep -q OKWORK <<<"$out" || ! grep -q OKTMP <<<"$out"; then say FAIL B7c "$(tr '\n' ' ' <<<"$out")"; else say PASS B7c "only /work and /tmp writable"; fi

# B10 inside --network=none: no resolver, no host addresses.
out=$(py none "
import socket
r=[]
try: socket.getaddrinfo('pypi.org',443); r.append('RESOLVED')
except OSError: r.append('noresolve')
for h,p in [('10.201.0.1',443),('192.168.1.210',22),('100.76.84.16',22),('127.0.0.1',3128),('10.42.0.1',443),('1.1.1.1',443)]:
    try: socket.create_connection((h,p),3); r.append('REACHED:%s:%d'%(h,p))
    except OSError: pass
print(' '.join(r))")
grep -q -E 'RESOLVED|REACHED' <<<"$out" && say FAIL B10 "network=none: $out" || say PASS B10 "network=none: nothing reachable ($out)"

# B10 with networking by mistake: pasta (default) and host networking both run as augexp or its subuids.
for net in pasta host; do
  before=$(nft list counter inet augexp augexp_drop | awk '/packets/{print $2}')
  out=$(py "$net" "
import socket
r=[]
for h,p in [('pypi.org',443),('1.1.1.1',443),('1.1.1.1',53),('10.201.0.1',443),('192.168.1.210',22)]:
    try: socket.create_connection((h,p),4); r.append('REACHED:%s:%d'%(h,p))
    except OSError as e: r.append('x')
print(' '.join(r))")
  after=$(nft list counter inet augexp augexp_drop | awk '/packets/{print $2}')
  if grep -q REACHED <<<"$out"; then say FAIL B10 "network=$net: $out"; else say PASS B10 "network=$net: nothing reachable; augexp_drop +$(( after - before ))"; fi
done

# B12: memory cap and pids limit stay inside the container.
out=$(py none "
print('memory.max', open('/sys/fs/cgroup/memory.max').read().strip(), 'swap.max', open('/sys/fs/cgroup/memory.swap.max').read().strip(), flush=True)
chunks=[]
try:
    for i in range(24):
        chunks.append(bytearray(b'\\x01') * (1<<30))   # written, so resident
        print('GiB', i+1, flush=True)
    print('ALLOCATED', len(chunks))
except MemoryError: print('MemoryError at', len(chunks))" ; echo "rc=$?")
last=$(grep -E '^GiB ' <<<"$out" | tail -1); mm=$(grep '^memory.max' <<<"$out")
if grep -q 'ALLOCATED 24' <<<"$out"; then say FAIL B12 "24 GiB resident under a 16g cap ($mm)"; else say PASS B12 "memory: $mm; stopped after ${last:-none}; $(grep -E '^rc=|MemoryError' <<<"$out" | tr '\n' ' ')"; fi
out=$(urun podman run $HARD --network=none --entrypoint python3 "$IMG" -c "
import os, time
n=0
try:
    for i in range(2000):
        if os.fork()==0: time.sleep(20); os._exit(0)
        n+=1
except OSError as e: print('fork stopped at', n, type(e).__name__)
else: print('FORKED', n)")
grep -q 'FORKED 2000' <<<"$out" && say FAIL B12 "pids: 2000 forks" || say PASS B12 "pids: $(tr '\n' ' ' <<<"$out")"
grep MemAvailable /proc/meminfo | awk '{print "INFO B12 host MemAvailable_kB", $2}'

# B14: sibling runs cannot see each other's /work, processes, /tmp or /dev/shm.
urun podman run --name bt-sibling-b $HARD --network=none -v "$RUNB:/work" --entrypoint sh "$IMG" -c 'echo secret-b > /work/b.txt; echo shm-b > /dev/shm/b; echo tmp-b > /tmp/b; sleep 60' >/dev/null &
BPID=$!
sleep 8
out=$(py none "
import os, glob
seen=[]
for p in ['$RUNB/b.txt','/work/b.txt','/dev/shm/b','/tmp/b']:
    try: open(p).read(); seen.append('READ:'+p)
    except OSError: pass
pids=[d for d in os.listdir('/proc') if d.isdigit()]
print('pids_visible=%d'%len(pids), ' '.join(seen))")
urun podman rm -f -t 0 bt-sibling-b >/dev/null; wait $BPID 2>/dev/null
grep -q 'READ:' <<<"$out" && say FAIL B14 "$out" || say PASS B14 "sibling not visible ($out)"

rm -rf "$RUNA" "$RUNB"
echo "SUMMARY fails=$fails"
exit $(( fails > 0 ))
