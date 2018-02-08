# Main build file for project. Used for both local builds and CI purposes.
#
# Requires automake, Python >= 3 and Docker installed in PATH, and accessible without sudo.
# First time after cloning project execute the following command to set up local virtualenv:
#
# $ make config
#
# After that builds can be started with just:
#
# $ make
#

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
