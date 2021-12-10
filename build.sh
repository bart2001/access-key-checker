#!/bin/bash

TAG="bart2001/access-key-checker:v0.0.0"

DOCKER_BUILDKIT=0 docker build -t ${TAG} .

docker push ${TAG}