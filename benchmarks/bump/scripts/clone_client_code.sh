#!/bin/bash

# To run the script in bump folder
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ../

if [ "$#" -ne 2 ]; then
    echo ":breakingUpdateID :path are missing"
    exit 1
fi

if ! [ -f "filtered_data/$1.json" ]; then
    echo "filtered_data/$1.json does not exists"
    exit 1
fi

if [ -d "$2" ]; then
    exit 0
fi

mkdir -p $2

# Saving old dependency version .jar file

project_id=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"project"' | awk  -F'"' '{print $4}')
dependencyGroupID=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"dependencyGroupID"' | awk  -F'"' '{print $4}')
dependencyArtifactID=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"dependencyArtifactID"' | awk  -F'"' '{print $4}')
previousVersion=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"previousVersion"' | awk  -F'"' '{print $4}')
dependency_path=$(echo "$dependencyGroupID" | tr . /)/$dependencyArtifactID/$previousVersion/$dependencyArtifactID-$previousVersion.jar

container_id=$(docker run -it --entrypoint /bin/sh -d "ghcr.io/chains-project/breaking-updates:$1-pre")
docker cp $container_id:/root/.m2/repository/$dependency_path $2
docker stop $container_id
docker remove $container_id


# Saving new dependency version .jar file and client code

newVersion=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"newVersion"' | awk  -F'"' '{print $4}')
dependency_path=$(echo "$dependencyGroupID" | tr . /)/$dependencyArtifactID/$newVersion/$dependencyArtifactID-$newVersion.jar

container_id=$(docker run -it --entrypoint /bin/sh -d "ghcr.io/chains-project/breaking-updates:$1-breaking")
docker cp $container_id:/$project_id $2
docker cp $container_id:/root/.m2/repository/$dependency_path $2
docker stop $container_id
docker remove $container_id