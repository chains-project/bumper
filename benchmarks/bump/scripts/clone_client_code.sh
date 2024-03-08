#!/bin/bash

# To run the script in bump folder
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ../

if [ "$#" -ne 1 ]; then
    echo "Breaking update ID is missing"
    exit 1
fi

if ! [ -f "filtered_data/$1.json" ]; then
    echo "filtered_data/$1.json does not exists"
    exit 1
fi

if [ -d "clients/$1" ]; then
    exit 0
fi

mkdir -p clients/$1

# Saving old dependency version .jar file

project_id=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"project"' | awk  -F'"' '{print $4}')
dependencyGroupID=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"dependencyGroupID"' | awk  -F'"' '{print $4}')
dependencyArtifactID=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"dependencyArtifactID"' | awk  -F'"' '{print $4}')
previousVersion=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"previousVersion"' | awk  -F'"' '{print $4}')
dependency_path=$(echo "$dependencyGroupID" | tr . /)/$dependencyArtifactID/$previousVersion/$dependencyArtifactID-$previousVersion.jar

docker run --name "$1" -it --entrypoint /bin/sh -d "ghcr.io/chains-project/breaking-updates:$1-pre" 
docker cp $1:/root/.m2/repository/$dependency_path clients/$1
docker stop $1
docker remove $1


# Saving new dependency version .jar file and client code

newVersion=$(cat filtered_data/$1.json | tr { '\n' | tr , '\n' | tr } '\n' | grep '"newVersion"' | awk  -F'"' '{print $4}')
dependency_path=$(echo "$dependencyGroupID" | tr . /)/$dependencyArtifactID/$newVersion/$dependencyArtifactID-$newVersion.jar

docker run --name "$1" -it --entrypoint /bin/sh -d "ghcr.io/chains-project/breaking-updates:$1-breaking" 
docker cp $1:/$project_id clients/$1
docker cp $1:/root/.m2/repository/$dependency_path clients/$1
docker stop $1
docker remove $1