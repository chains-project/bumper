#!/bin/bash

# To run the script in bump folder
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ../

if [ "$#" -ne 2 ]; then
    echo "ERROR: not enough parameters."
    echo "use cleanup_after_failure.sh :BreakingUpdateID"
    exit 1
fi

docker stop $1
docker remove $1
exit 0