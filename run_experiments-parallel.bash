#!/bin/bash

trap 'kill $(jobs -p)' EXIT

if [ "$#" -ne 1 ]; then
    echo "ERROR: not enough parameters."
    echo "use run_experiments.bash :name"
    exit 1
fi

RUN_ID="gpt4" WITHOUT_APIDIFF="True" python benchmark.py -n "$1_without_diff" -m gpt4 -p advanced &
RUN_ID="mixtral" WITHOUT_APIDIFF="True" python benchmark.py -n "$1_without_diff" -m mixtral -p standard &
wait
git add . && git commit -m "[Benchmark $1] update results" && git push

RUN_ID="gpt4" WITHOUT_APIDIFF="False" python benchmark.py -n "$1_with_diff" -m gpt4 -p advanced &
RUN_ID="mixtral" WITHOUT_APIDIFF="False" python benchmark.py -n "$1_with_diff" -m mixtral -p standard &
wait
git add . && git commit -m "[Benchmark $1] update results" && git push