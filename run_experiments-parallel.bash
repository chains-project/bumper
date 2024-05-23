#!/bin/bash

trap 'kill $(jobs -p)' EXIT

pipelines=("baseline" "standard" "advanced")
models=("gpt4" "gemini" "mixtral" "llama")

if [ "$#" -ne 1 ]; then
    echo "ERROR: not enough parameters."
    echo "use run_experiments.bash :name"
    exit 1
fi

run_benchmark() {
  echo "[$1] Running $2 with WITHOUT_APIDIFF=$3"
  WITHOUT_APIDIFF=$without_diff python benchmark.py -n "$1_$4" -m gpt4 -p $pipeline &
  WITHOUT_APIDIFF=$without_diff python benchmark.py -n "$1_$4" -m gemini -p $pipeline &
  WITHOUT_APIDIFF=$without_diff python benchmark.py -n "$1_$4" -m mixtral -p $pipeline &
  WITHOUT_APIDIFF=$without_diff python benchmark.py -n "$1_$4" -m llama -p $pipeline &
  wait

}

for pipeline in ${pipelines[@]}; do
  run_benchmark $1 $pipeline "True" "without_diff"
  git add . && git commit -m "[Benchmark $1] update results" && git push
  run_benchmark $1 $pipeline "False" "with_diff"
  git add . && git commit -m "[Benchmark $1] update results" && git push
done