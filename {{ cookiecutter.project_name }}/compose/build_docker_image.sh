#!/bin/bash
set -e

source VERSION

cp -r ../requirements ./
{
    docker build . -t "${DOCKER_IMAGE}:${DOCKER_IMAGE_VERSION}"
} || {
    echo "build failed"
}
rm -r requirements
