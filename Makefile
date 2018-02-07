all: vendor test package

config:
	@rm -rf .venv && python -m venv .venv

vendor:
	@bash .build/vendor.sh

test:
	@bash .build/test.sh

package:
	@bash .build/package.sh

.PHONY: all vendor test package