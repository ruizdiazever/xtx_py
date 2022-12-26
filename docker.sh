#!/usr/bin/env bash

# Docker
docker image build -t redchiche .           # Build with detach mode in .
echo 'IMAGE OF DOCKER BUILDED'                # INFO
docker run -td redchiche                      # RUN in background
echo 'READY AND RUNNING IN BACKGROUND'