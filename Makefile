all: vendor test

config:
	@rm -rf .venv && python -m venv .venv

vendor:
	@bash .build/vendor.sh

test:
	@bash .build/test.sh

.PHONY: all vendor test