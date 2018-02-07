all: vendor test

config:
	@rm -rf .venv && python -m venv .venv

vendor:
	@source ./.venv/bin/activate && python -m pip install -r requirements.txt

test:
	@source ./.venv/bin/activate && python -m nose

.PHONY: all vendor test