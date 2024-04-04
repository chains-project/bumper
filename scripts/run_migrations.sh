#!/bin/bash

for script in ./scripts/migrations/*.bash ; do
    echo "----------- $(basename "$script") -----------"
    bash $script $1 || exit
done

