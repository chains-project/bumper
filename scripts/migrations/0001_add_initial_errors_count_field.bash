#!bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" || exit ; pwd -P )
cd "$parent_path" || exit
cd ../..

jq 'to_entries | map_values(.value += { "initial_errors_count": 0 }) | from_entries' $1 > $1