#!/bin/bash
docker build -t turbinia-client:$1 .
docker tag turbinia-client:$1  gcr.io/oss-forensics-registry/turbinia/turbinia-client:$1
