#!/bin/bash
docker build -t fraken:$1 .
docker tag fraken:$1 us-docker.pkg.dev/osdfir-registry/fraken/release/fraken:$1
