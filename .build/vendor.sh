#!/bin/bash

source "./.venv/bin/activate"

files=$(find . -name "requirements.txt" -type f)

for file in ${files}; do
    python -m pip install -r ${file}
done
