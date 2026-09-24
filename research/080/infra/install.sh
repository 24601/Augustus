#!/bin/bash
# Install the Augustus 0.8.0 containment on tabputer-1: the egress table (inet augexp), the
# local-IPC denials, the setup proxy and the window script. Run as root from the unpacked
# bundle directory. It loads only table inet augexp and never flushes the ruleset. It arms a
# 5-minute dead-man that deletes the table and leaves a marker, unless cancelled after a
# fresh SSH login is confirmed from outside.
set -euo pipefail
[[ $EUID -eq 0 ]] || { echo "run as root" >&2; exit 1; }
cd "$(dirname "$0")"
[[ "$(id -u augexp)" == 48201 && "$(id -u augctl)" == 48202 && "$(id -u augproxy)" == 947 ]] \
  || { echo "uid mismatch with augexp.nft" >&2; exit 1; }
sha256sum -c SHA256SUMS
for m in /etc/augustus/DEADMAN_FIRED /etc/augustus/CONTAINMENT_FAILED; do
  [[ -e "$m" ]] && { echo "marker $m exists: investigate, then remove it before re-installing" >&2; exit 1; }
done
grep -q '^augexp:165536:65536$' /etc/subuid && grep -q '^augexp:165536:65536$' /etc/subgid \
  || { echo "augexp subuid/subgid range differs from augexp.nft" >&2; exit 1; }
grep -qE '^(augctl|augproxy):' /etc/subuid /etc/subgid && { echo "augctl/augproxy must have no subuids" >&2; exit 1; } || true

# The principal uids must belong to no other workload: skuid matches every socket in the
# host netns with that uid, and a shared uid would expose the other workload's /proc.
bad=0
while read -r uid pid cg; do
  case "$uid" in
    48201) [[ "$cg" == */user.slice/user-48201.slice/* ]] || { echo "uid 48201 used outside augexp's slice: pid $pid $cg" >&2; bad=1; } ;;
    48202) echo "uid 48202 has a running process: pid $pid $cg" >&2; bad=1 ;;
    947)   [[ "$cg" == */system.slice/augproxy.service ]] || { echo "uid 947 used outside augproxy.service: pid $pid $cg" >&2; bad=1; } ;;
  esac
done < <(for p in /proc/[0-9]*; do
           u=$(awk '/^Uid:/{print $2}' "$p/status" 2>/dev/null) || continue
           if (( u >= 165536 && u <= 231071 )); then u=48201; fi
           [[ "$u" == 48201 || "$u" == 48202 || "$u" == 947 ]] || continue
           echo "$u ${p#/proc/} $(head -1 "$p/cgroup" 2>/dev/null | cut -d: -f3)"
         done)
owned=$(ss -tuneapH 2>/dev/null | grep -oE 'uid:[0-9]+' | cut -d: -f2 | sort -un \
  | awk '$1==48201 || $1==48202 || $1==947 || ($1>=165536 && $1<=231071)')
[[ -z "$owned" ]] || { echo "sockets already owned by principal uids: $owned" >&2; bad=1; }
[[ $bad -eq 0 ]] || { echo "refusing to load: principal uid collision" >&2; exit 1; }

install -d -m 755 /etc/augustus /usr/local/lib/augustus /etc/dbus-1/system.d
install -m 644 nft/augexp.nft /etc/augustus/augexp.nft
install -m 644 augproxy/allowlist.txt /etc/augustus/augproxy.allowlist
install -m 644 augproxy/augproxy.py /usr/local/lib/augustus/augproxy.py
install -m 755 sbin/augwindow /usr/local/sbin/augwindow
install -m 755 sbin/augipc-acl /usr/local/sbin/augipc-acl
install -m 755 sbin/augfs-deny /usr/local/sbin/augfs-deny
install -m 644 dbus/augustus.conf /etc/dbus-1/system.d/augustus.conf
install -d -o augproxy -g augproxy -m 750 /var/log/augproxy
for u in augexp-nft augproxy augipc-acl augexp-alarm; do
  install -m 644 "systemd/$u.service" "/etc/systemd/system/$u.service"
done
for d in systemd/dropins/*.conf; do
  unit=$(basename "$d" .conf)
  install -d -m 755 "/etc/systemd/system/$unit.d"
  install -m 644 "$d" "/etc/systemd/system/$unit.d/augustus-acl.conf"
done
nft -c -f /etc/augustus/augexp.nft
systemctl daemon-reload

# Local IPC and other workloads' trees first: no network change, cannot lock anyone out.
/usr/local/sbin/augipc-acl
/usr/local/sbin/augfs-deny
systemctl enable --now augipc-acl.service
busctl call org.freedesktop.DBus /org/freedesktop/DBus org.freedesktop.DBus ReloadConfig

# Egress table, with a dead-man that fails loudly.
systemctl stop augexp-nft-deadman.timer 2>/dev/null || true
systemctl reset-failed augexp-nft-deadman.service augexp-nft-deadman.timer 2>/dev/null || true
systemd-run --unit=augexp-nft-deadman --on-active=300 /bin/sh -c \
  'nft delete table inet augexp; logger -p auth.crit augexp-deadman-fired; touch /etc/augustus/DEADMAN_FIRED'
systemctl restart augexp-nft.service
systemctl enable augexp-nft.service
nft list table inet augexp | head -5
echo "DEAD-MAN ARMED: confirm a fresh ssh, then: systemctl stop augexp-nft-deadman.timer"
