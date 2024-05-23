#!/bin/bash

# To run the script in bump folder
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ../

if [ "$#" -ne 3 ]; then
    echo "ERROR: not enough parameters."
    echo "use test_patched_code.sh :BreakingUpdateID :PatchedCodePath :containerID"
    exit 1
fi

if ! [ -f "filtered_data/$1.json" ]; then
    echo "filtered_data/$1.json does not exists"
    exit 1
fi

patched_version_path=$2

docker run --name "$3" --platform linux/amd64 -i --entrypoint /bin/sh -d "ghcr.io/chains-project/breaking-updates:$1-breaking"
docker cp $patched_version_path $3:/
docker exec -i $3 mvn clean test -B | tee $patched_version_path/$1.log
docker stop $3
docker remove $3

if [ "$(cat $patched_version_path/$1.log | grep -c "BUILD SUCCESS")" -gt 0 ]; then
  exit 0
else
  exit 1
fi
