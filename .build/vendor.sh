#!/bin/bash

set -e

bundles=$(find . -name "requirements.txt" -type f)

for bundle in ${bundles}; do
    echo "installing external dependencies from ${bundle}..."
    ./.venv/bin/python -m pip install -r "${bundle}"
done
