---
title: "Augustus v0.7.2: check provider terms before training on provider outputs"
description: "A patch that stops the skill from suggesting provider outputs as distillation targets without a terms check, and names TypeSafe's restriction on training with Jev Output."
permalink: /release-notes-v0.7.2.html
---

# Augustus v0.7.2

Released 2026-09-23. This patch corrects one piece of guidance. It adds no
capability and changes no interface, reference path, or script.

## What changed

The specialist-training guidance in `optimizer-integration.md` said training
"may use provider or teacher distributions as features, weak labels, or
distillation targets". TypeSafe Jev is this skill's default hosted exemplar,
and TypeSafe's [Master Customer Agreement](https://typesafe.ai/legal/mca)
§2.3(b), updated Sep 19, 2026, says the customer will not "use the Services or
any Output ... to perform model distillation, train a model to imitate the
output of the Services, or develop (or to facilitate the development of) a
similar or competing product or service."

The guidance now:

- requires a terms check before any provider output enters a training path,
  whether as labels, targets, features, filtering, or example selection;
- names TypeSafe's restriction;
- treats every training path as covered unless the contract owner confirms a
  use is allowed.

The uncertainty-selection pattern and the template's optional teacher features
carry the same condition. A new `provider_distillation` scenario checks the
behavior.

This states the contract text and a conservative engineering rule. It is not a
legal interpretation; confirm your own agreement with its owner.

## Evidence and limits

A fresh agent answered `provider_distillation` and `distillation_errors` on the
exact release text. Fable 5.1 graded both answers and found no blocking issue.
Its one precision note separated the quoted contract text from the
conservative rule, and it was applied before release. The clause was read from
the live agreement page on 2026-09-23 (HTML sha256 prefix `b07b91d9`). No
provider call was made.

Upgrade by reinstalling from the `v0.7.2` tag. A Claude Code marketplace pinned
to an earlier tag needs `claude plugin marketplace remove augustus`, then add
`24601/Augustus@v0.7.2` and install again.

Earlier release: [v0.7.1]({{ '/release-notes-v0.7.1.html' | relative_url }}).
