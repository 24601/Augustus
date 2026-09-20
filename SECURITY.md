# Security

## Supported versions

| Version | Supported |
| ------- | --------- |
| 0.5.x   | Yes       |
| 0.4.x   | No        |
| < 0.4   | No        |

This repo is a design-judgment skill plus offline scripts. There is no
hosted API and no runtime that accepts untrusted input by default.

## Report a vulnerability

Use GitHub **Security Advisories** / private vulnerability reporting on
this repository:

https://github.com/24601/Augustus/security/advisories/new

Do not open a public issue for a security report. There is no separate
security email.

Please include what is affected (skill text, evaluator, workflows, Pages)
and a way to reproduce. We will acknowledge and ship a fix on the
supported line when the report is valid.

## Already enabled (do not disable)

- Dependabot security updates
- Secret scanning
- Push protection for secrets

## Secrets

Do not commit API keys, tokens, or `.env` files. `.gitignore` covers the
common names. Research folds quote public READMEs; they are not install
recipes and must not paste live credentials.

`evaluate_decisions.py --self-test` is local scoring math. It does not
call a model and does not need a key.
