#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" || exit ; pwd -P )
cd "$parent_path" || exit

if ! [ -d './repository' ]; then
    git clone https://github.com/chains-project/bump.git ./repository
fi

# First step: filter data from benchmark
mkdir -p filtered_data

for file in ./repository/data/benchmark/*.json; do
    if grep -q "COMPILATION_FAILURE" $file; then
        cp $file "./filtered_data/$(basename $file)"
    fi
done

original_files_count=$(ls -1q ./repository/data/benchmark/* | wc -l)
filtered_files_count=$(ls -1q ./filtered_data/* | wc -l)

echo "kept $filtered_files_count / $original_files_count files for failure type"
echo "filtering size and compilation type"

python filter.py

echo "bump config done."



