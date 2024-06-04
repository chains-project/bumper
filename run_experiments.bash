#!/bin/bash

pipelines=("baseline" "standard" "advanced")
models=("gpt4" "gemini" "mixtral" "llama")

if [ "$#" -ne 1 ]; then
    echo "ERROR: not enough parameters."
    echo "use run_experiments.bash :name"
    exit 1
fi

# Without API Diff
for pipeline in ${pipelines[@]}; do
  for model in ${models[@]}; do
    echo "[$1] Running $pipeline with $model model without API Diff"
    WITHOUT_APIDIFF=True python benchmark.py -n "$1_without_diff" -m $model -p $pipeline
#    git add . && git commit -m "[Benchmark $1] update results" && git push
    sleep 10
  done
done

# With API Diff
for pipeline in ${pipelines[@]}; do
  for model in ${models[@]}; do
    echo "[$1] Running $pipeline with $model model with API Diff"
    WITHOUT_APIDIFF=False python benchmark.py -n "$1_with_diff" -m $model -p $pipeline
#    git add . && git commit -m "[Benchmark $1] update results" && git push
    sleep 10
  done
done
