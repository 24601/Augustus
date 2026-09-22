PYTHON ?= python3

.PHONY: check
check:
	$(PYTHON) scripts/check_repo.py
	$(PYTHON) -m unittest discover -s tests -v
	$(PYTHON) .agents/skills/augustus/scripts/evaluate_decisions.py --self-test
	$(PYTHON) research/revisit_fingerprints.py --self-test
	bash -n scripts/hourly-refresh.sh scripts/refresh-jev-research.sh
