#!/bin/bash

source "./.venv/bin/activate"

packages=$(find . -name "setup.py" -type f -printf "%h\n")

for package in ${packages}; do
    echo "running tests for ${package}..."
    python -m nose "${package}"
done
