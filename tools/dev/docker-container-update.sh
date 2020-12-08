#!/bin/bash
#
# Script to build, tag, push a new server/worker docker container and 
# (optionally) update a running GCE container instance.
# Usage examples
# Build a worker Docker image and push it to GCP:
# $ ./docker-container-update.sh my-test-project worker
# Build a server Docker image, push it to GCP and update a GCE container instance with that image
# $ ./docker-container-update.sh my-test-project server turbinia-server-495940302 us-central1-f

set -e

if [[ -z "$2" ]]; then
    echo "Usage: $0 <gcp-project> <worker|server> [<gce-instance-id> <gce-instance-zone>]"
    echo "  where <gce-instance-id> and <gce-instance-zone> are optional."
    exit 1
fi

PROJECT=$1
TYPE=$2
INSTANCE=$3
ZONE=$4

if [ -z "$3" ]; then
    echo "No GCE instance info given so not updating any GCE containers"
fi

if [[ ! -f "docker/$TYPE/Dockerfile" ]]; then
    echo "File 'docker/$TYPE/Dockerfile' not found!"
    echo "Make sure you run this tool from the Turbinia source root."
    exit 1
fi

TAG=`date +%s`

docker build -t turbinia-$TYPE:$TAG -f docker/$TYPE/Dockerfile .
docker tag turbinia-$TYPE:$TAG gcr.io/$PROJECT/turbinia/turbinia-$TYPE:$TAG
docker push gcr.io/$PROJECT/turbinia/turbinia-$TYPE:$TAG
if [ -z "$3" ] && [ -z "$4" ]; then
    gcloud --project=$PROJECT compute instances update-container $INSTANCE --zone=$ZONE --container-image=gcr.io/$PROJECT/turbinia/turbinia-$TYPE:$TAG
fi
