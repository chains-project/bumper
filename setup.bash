#!/bin/bash

# First, clone the BUMP repository
echo "Setting up benchmarks..."
for directory in ./benchmarks/* ; do
    cd "$directory" || exit
    echo "----------- $(basename "$directory") -----------"
    bash "setup.sh"
    cd "$OLDPWD" || exit
done
echo "Benchmarks setup completed."

