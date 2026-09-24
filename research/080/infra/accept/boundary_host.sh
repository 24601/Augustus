#!/bin/bash
# Plan v3 §4.3 host-side boundary tests B1-B8, B11 and B15 for augexp and augctl on tabputer-1.
# Run as root. Each test prints one line: RESULT test principal detail. PASS means the boundary
# held. Nothing here writes outside /srv/aug/admin, /tmp/augbt-* and the principals' homes, and
# every probe file it creates is removed.
set -uo pipefail
[[ $EUID -eq 0 ]] || { echo "run as root" >&2; exit 1; }
MAINT=basit
MHOME=$(getent passwd "$MAINT" | cut -d: -f6)
fails=0
say() { printf '%s %s %s %s\n' "$1" "$2" "$3" "$4"; [[ $1 == PASS ]] || fails=$((fails+1)); }
as() { local who=$1; shift; sudo -n -u "$who" -H bash -c "cd /tmp; $*" 2>&1; }

CANARY="augbt-canary-$(head -c 12 /dev/urandom | od -An -tx1 | tr -d ' \n')"
install -o augctl -g augctl -m 600 /dev/null /srv/aug/ctl/canary.txt
echo "$CANARY" > /srv/aug/ctl/canary.txt

for P in augexp augctl; do
  # B1: no admin groups, sudo and polkit denied.
  g=$(id -nG "$P")
  if grep -qwE 'wheel|sudo|docker|adm|systemd-journal|libvirt|kvm|lxd' <<<"$g"; then say FAIL B1 "$P" "groups: $g"; else say PASS B1 "$P" "groups: $g"; fi
  if as "$P" "sudo -n true" >/dev/null 2>&1; then say FAIL B1 "$P" "sudo -n true succeeded"; else say PASS B1 "$P" "sudo denied"; fi
  out=$(as "$P" "pkcheck --action-id org.freedesktop.systemd1.manage-units --process \$\$ 2>&1; echo rc=\$?")
  grep -q 'rc=0' <<<"$out" && say FAIL B1 "$P" "polkit manage-units allowed" || say PASS B1 "$P" "polkit manage-units denied"

  # B2: credential inventory in the principal's own home and environment.
  cred=$(as "$P" 'ls -d ~/.ssh ~/.netrc ~/.git-credentials ~/.config/gh ~/.cache/huggingface/token ~/.huggingface ~/.docker ~/.kube ~/.aws ~/.codex 2>/dev/null; env | grep -v -E "^SUDO_" | grep -E "_(TOKEN|KEY)=|SECRET" | cut -d= -f1')
  [[ -z "$cred" ]] && say PASS B2 "$P" "none" || say FAIL B2 "$P" "found: $(tr '\n' ' ' <<<"$cred")"

  # B3: the maintainer's home and /root.
  n=$(as "$P" "find '$MHOME' /root -maxdepth 3 -type f -readable 2>/dev/null | head -50 | wc -l")
  ls_h=$(as "$P" "ls '$MHOME' >/dev/null 2>&1 && echo listable || echo denied")
  [[ "$n" == 0 ]] && say PASS B3 "$P" "0 readable files; home $ls_h" || say FAIL B3 "$P" "$n readable files under $MHOME or /root; home $ls_h"

  # B4: other workloads.
  hits=""
  for f in /etc/rancher/k3s/k3s.yaml /var/lib/rancher /var/lib/kubelet /var/lib/docker /var/lib/containers /run/k3s \
           /var/run/docker.sock /run/containerd/containerd.sock "/run/user/$(id -u $MAINT)" /var/lib/ollama /usr/share/ollama/.ollama \
           /etc/systemd/system/ollama.service.d; do
    [[ -e "$f" ]] || continue
    r=$(as "$P" "if [[ -d '$f' ]]; then ls '$f' >/dev/null 2>&1 && echo R; elif [[ -S '$f' ]]; then [[ -w '$f' ]] && echo R; else head -c1 '$f' >/dev/null 2>&1 && echo R; fi")
    [[ "$r" == R ]] && hits+="$f "
  done
  as "$P" "docker ps >/dev/null 2>&1" && hits+="docker-ps "
  as "$P" "k3s kubectl get pods -A >/dev/null 2>&1 || kubectl get pods -A >/dev/null 2>&1" && hits+="kubectl "
  [[ -z "$hits" ]] && say PASS B4 "$P" "all refused" || say FAIL B4 "$P" "reachable: $hits"

  # B5: machine-wide readable files outside /usr /proc /sys, own home and stage, grepped for secret markers.
  pat='(-----BEGIN [A-Z ]*PRIVATE KEY-----|hf_[A-Za-z0-9]{30,}|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-[A-Za-z0-9_-]{32,}|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|tskey-[A-Za-z0-9-]{20,}|TYPESAFE_API_KEY=.+)'
  home=$(getent passwd "$P" | cut -d: -f6)
  b5=$(as "$P" "find / -xdev \\( -path /usr -o -path /proc -o -path /sys -o -path '$home' -o -path /srv/aug/stage -o -path /dev \\) -prune -o -type f -readable -size -2M -print 2>/dev/null \
        | grep -v -E '^/(etc/(ssl|ca-certificates|pki)|var/lib/pacman/sync)/' \
        | xargs -d '\n' -r grep -l -I -E '$pat' 2>/dev/null | head -20")
  for d in /tmp /dev/shm /run; do
    b5+=$(as "$P" "find '$d' -type f -readable -size -2M 2>/dev/null | xargs -d '\n' -r grep -l -I -E '$pat' 2>/dev/null | head -10")
  done
  if [[ -z "$b5" ]]; then say PASS B5 "$P" "0 hits"; else
    classes=""
    while read -r f; do
      [[ -n "$f" ]] || continue
      c=""
      for k in 'BEGIN [A-Z ]*PRIVATE KEY' 'hf_[A-Za-z0-9]{30,}' 'gh[pousr]_[A-Za-z0-9]{30,}' 'github_pat_' 'sk-[A-Za-z0-9_-]{32,}' 'xox[baprs]-' 'AKIA[0-9A-Z]{16}' 'tskey-' 'TYPESAFE_API_KEY='; do
        grep -q -I -E "$k" "$f" 2>/dev/null && c+="${k%%[\[ ]*} "
      done
      classes+="$f[$c] "
    done <<<"$b5"
    # A PEM marker only counts when a key body follows it; docs and magic-byte tables quote the
    # marker without one. Other classes always count. Only yes/no is printed, never content.
    real=""
    while read -r f; do
      [[ -n "$f" ]] || continue
      if python3 - "$f" <<'PY'
import re, sys
t = open(sys.argv[1], "rb").read().decode("latin-1")
other = re.search(r"hf_[A-Za-z0-9]{30,}|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-[A-Za-z0-9_-]{32,}|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|tskey-[A-Za-z0-9-]{20,}|TYPESAFE_API_KEY=.+", t)
pem = re.search(r"-----BEGIN [A-Z ]*PRIVATE KEY-----\s*(?:\\n|\n)\s*[A-Za-z0-9+/=]{40,}", t)
sys.exit(0 if (other or pem) else 1)
PY
      then real+="$f "; fi
    done <<<"$b5"
    if [[ -z "$real" ]]; then say PASS B5 "$P" "0 real hits ($(wc -l <<<"$b5") marker-only files: $classes)"; else say FAIL B5 "$P" "real hits: $real"; fi
  fi

  # B8: persistence. crontab refused or absent; no user unit can be enabled outside a window.
  cr=$(as "$P" "command -v crontab >/dev/null && (echo '* * * * * true' | crontab - 2>&1; crontab -l 2>&1; crontab -r 2>/dev/null) || echo 'no crontab binary'")
  if grep -q '^\* \* \* \* \* true' <<<"$cr"; then say FAIL B8 "$P" "crontab accepted (removed)"; else say PASS B8 "$P" "crontab: $(head -1 <<<"$cr" | cut -c1-60)"; fi
  if [[ -e /var/lib/systemd/linger/$P ]]; then say INFO B8 "$P" "linger ON (allowed only inside a window)"; else say PASS B8 "$P" "no linger"; fi
done

# B6: augexp cannot read /srv/aug/ctl or the canary.
out=$(as augexp "cat /srv/aug/ctl/canary.txt; ls /srv/aug/ctl; grep -r '$CANARY' /srv/aug 2>/dev/null")
grep -q "$CANARY" <<<"$out" && say FAIL B6 augexp "canary read" || say PASS B6 augexp "ctl EACCES; canary not seen"
out=$(as augexp "grep -rl '$CANARY' /srv /tmp /home 2>/dev/null | head -3")
[[ -z "$out" ]] && say PASS B6 augexp "canary absent from readable trees" || say FAIL B6 augexp "canary in: $out"

# B7: writes the principals must not make (host side; container side is tested in boundary_container.sh).
for P in augexp augctl; do
  bad=""
  for d in "$MHOME" /srv/aug/stage /srv/aug/stage/models /srv/aug/inbox /etc /usr /usr/local/bin /opt/rocm /srv/aug/admin; do
    as "$P" "touch '$d/.augbt-w' 2>/dev/null && rm -f '$d/.augbt-w' && echo W" | grep -q W && bad+="$d "
  done
  [[ "$P" == augexp ]] && { as augexp "touch /srv/aug/ctl/.augbt-w 2>/dev/null && echo W" | grep -q W && bad+="/srv/aug/ctl "; }
  [[ "$P" == augctl ]] && { as augctl "touch /srv/aug/runs/.augbt-w /srv/aug/pred/.augbt-w 2>/dev/null && echo W" | grep -q W && bad+="runs/pred "; }
  [[ -z "$bad" ]] && say PASS B7 "$P" "all refused" || say FAIL B7 "$P" "writable: $bad"
done

# B11: augctl reaches nothing (egress counters were checked separately; repeat one probe).
as augctl "timeout 5 bash -c 'exec 3<>/dev/tcp/127.0.0.1/3128' 2>/dev/null && echo C" | grep -q C && say FAIL B11 augctl "proxy port reachable" || say PASS B11 augctl "connect refused/dropped"

# B15: principal uids used by nothing else.
b15=""
for p in /proc/[0-9]*; do
  u=$(awk '/^Uid:/{print $2}' "$p/status" 2>/dev/null) || continue
  cg=$(head -1 "$p/cgroup" 2>/dev/null | cut -d: -f3)
  if [[ "$u" == 48201 ]] || { (( u >= 165536 && u <= 231071 )); }; then
    [[ "$cg" == */user.slice/user-48201.slice/* ]] || b15+="${p#/proc/}($u:$cg) "
  elif [[ "$u" == 48202 ]]; then b15+="${p#/proc/}($u:$cg) "
  elif [[ "$u" == 947 ]]; then [[ "$cg" == */system.slice/augproxy.service ]] || b15+="${p#/proc/}($u:$cg) "
  fi
done
[[ -z "$b15" ]] && say PASS B15 all "no foreign process on principal uids" || say FAIL B15 all "$b15"

rm -f /srv/aug/ctl/canary.txt
echo "SUMMARY fails=$fails"
exit $(( fails > 0 ))
