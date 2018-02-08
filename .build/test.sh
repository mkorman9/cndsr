#!/bin/bash

packages=$(find . -name "setup.py" -type f -printf "%h\n")

for package in ${packages}; do
    echo "running tests for ${package}..."
    ./.venv/bin/python -m nose "${package}"
done
