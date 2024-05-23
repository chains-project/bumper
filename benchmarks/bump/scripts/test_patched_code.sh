#!/bin/bash

# To run the script in bump folder
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ../

if [ "$#" -ne 2 ]; then
    echo "ERROR: not enough parameters."
    echo "use test_patched_code.sh :BreakingUpdateID :PatchedCodePath"
    exit 1
fi

if ! [ -f "filtered_data/$1.json" ]; then
    echo "filtered_data/$1.json does not exists"
    exit 1
fi

mkdir -p clients/$1

# Saving old dependency version .jar file
project_id=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"project"' | awk  -F'"' '{print $4}')
patched_version_path=$2

docker run --name "$1" --platform linux/amd64 -it --entrypoint /bin/sh -d "ghcr.io/chains-project/breaking-updates:$1-breaking"
docker cp $patched_version_path $1:/
docker exec -it $1 mvn clean test -B | tee $patched_version_path/$1.log
docker stop $1
docker remove $1

if [ "$(cat $patched_version_path/$1.log | grep -c "BUILD SUCCESS")" -gt 0 ]; then
  exit 0
else
  exit 1
fi
