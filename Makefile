# Main build file for project. Used for both local builds and CI purposes.
#
# Requires GNU tools, Python >= 3, Docker and docker-compose installed, and accessible through PATH without sudo.
# NOTE: On Unix-like systems it is required to install GNU findutils.
# On macOS simply brew install findutils and modify PATH. Popular Linux distribution should come with it already.
#
# How to build?
# First time after cloning project execute the following command to set up local virtualenv:
#
# $ make config
#
# After that builds can be started with just:
#
# $ make
#
# Feature tests can be started with:
#
# $ make validate
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

validate:
	@bash .build/validate.sh

.PHONY: all vendor test package validate
