#!/bin/bash

images=$(find $(pwd) -type f -name '.image' -printf "%h\n" | sort | uniq)
image_version=${VERSION:-0.0.0-dev}

for image in ${images}; do
    image_tag=$(cat "${image}/.image")
    tag_with_version="${image_tag}:${image_version}"

    echo "packaging $image_tag:$image_version..."

    docker build \
        -f ${image}/Dockerfile \
        --tag="${tag_with_version}" \
        .

    docker tag "${tag_with_version}" "${image_tag}:latest"
done