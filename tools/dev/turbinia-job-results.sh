#!/bin/bash
#
# Script to fetch all Turbinia request results from GCS.
# Usage example
# Fetch all results from Turbinia request id 12345678
# $ ./turbinia-job-results.sh 12345678

echo "Make sure you run this tool from the Turbinia source root."

if [[ -z "$1" ]]; then
    echo "Usage: $0 <turbinia-request-id>"
    exit 1
fi

DETAIL_LOG=$1.log
LOGS=$1-logs
PYTHONPATH=. python3 turbinia/turbiniactl.py -d -a status -r $1 -R > $DETAIL_LOG

mkdir $LOGS

echo "Copy all task result files from GCS"

cat $DETAIL_LOG|grep "gs://"|tr -d "*\`"|while read line
do
  OUTFILE=`echo "$line"|awk -F/ '{print $(NF-1)"_"$NF}'`
  echo "Copying $line to $OUTFILE"
  gsutil cp $line $LOGS/$OUTFILE
done
mv $DETAIL_LOG $LOGS/