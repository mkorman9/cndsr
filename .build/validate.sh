#!/bin/bash

cd "./feature-tests"

echo "starting feature tests..." && \
    docker-compose up --abort-on-container-exit --exit-code-from feature-tests && \
    status="$?" && \
    echo "finished running feature tests. status: $status" && \
    docker-compose down

if [[ "$status" != "0" ]]; then
    echo "feature tests failed!"
    exit 1
else
    echo "feature tests passed"
    exit 0
fi
