#!/bin/bash

images=$(find $(pwd) -type f -name '.image' -printf "%h\n" | sort | uniq)
build_key=$(cat /dev/urandom | head -c 32 | base64 | tr -dc _A-Z-a-z-0-9)
image_version=${VERSION:-0.0.0-dev}

for image in ${images}; do
    image_tag=$(cat "${image}/.image")
    tag_with_version="${image_tag}:${image_version}"

    echo "packaging $image_tag:$image_version..."

    docker build \
        -f ${image}/Dockerfile \
        --tag="${tag_with_version}" \
        --build-arg BUILD_KEY="$build_key" \
        .

    docker tag "${tag_with_version}" "${image_tag}:latest"
done
