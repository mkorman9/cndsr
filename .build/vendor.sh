#!/bin/bash

source "./.venv/bin/activate"

bundles=$(find . -name "requirements.txt" -type f)

for bundle in ${bundles}; do
    echo "installing external dependencies from ${bundle}..."
    python -m pip install -r "${bundle}"
done
