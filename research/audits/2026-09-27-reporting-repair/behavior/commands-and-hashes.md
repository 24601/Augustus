# Behavioral execution evidence — 2026-09-27

Fresh-agent run. Only `.agents/skills/augustus-train/SKILL.md` plus its linked
references and `scripts/policy_receipt.py` were read. Executable work ran in /tmp/beh.

## Commands

```sh
mkdir -p /tmp/beh && cd /tmp/beh   # policy-input.json written (copy in this folder)
TRAINER=/home/user/workspace/repo/.agents/skills/augustus-train
python3 "$TRAINER/scripts/policy_receipt.py" policy-input.json > policy-receipt.json   # exit 0
```

## sha256 of skill files read

```
6fa43a430ac767381e704e52ccce5474cbbb3d569ed422e45213c20e45b0a485  SKILL.md
7c38c10e733ff84d4f8cb72225b32bad2dfa23260d82491e489aa5a25eec8b35  references/compute-envelope.md
4ef9700080ba8b6904b6207fee39e3bd6dbf62d07ede03689d21aab6117b16a4  references/data-and-splits.md
5ade9865a8df7c3e7674df15f9187238a516f94e1af6ac0798deff3aa66288a3  references/fit-and-serve.md
96158be50be37434ee283f2557c6cfed2faebda090060574992d70a549176248  references/improve-and-confirm.md
245a9d13bcd4d22bc9806db1b4c8947db307028719f92a15125bab11ec94234e  references/spec-defects.md
6bafc5ae4fd33cc0d969924f987cc045b202a4d2da3fffc61b6479bd225d778e  scripts/policy_receipt.py
```

Receipt input sha256 `9faa88390279b4777fd59412bb888672df3edfdf386fa57946a183188916280b`;
selected-rows sha256 `8684dac8bf424053c292756f1d77455031b06dad5a19159324395ebfaca27e06`.
Note: compute-envelope.md and data-and-splits.md hashed but only skimmed via SKILL routing;
no API calls, no evaluations, no deployment performed.
