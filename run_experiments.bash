#!/bin/bash

pipelines=("baseline", "standard")
models=("gpt4", "gemini", "mixtral", "llama")

# Without API Diff
for pipeline in ${pipelines[@]}; do
  for model in ${models[@]}; do
    echo "Running $pipeline with $model model without API Diff"
    WITHOUT_APIDIFF=True python benchmark.py -n without_diff -m $model -p $pipeline
    git add . && git commit -m "[Benchmark] update results" && git push
  done
done

# With API Diff
for pipeline in ${pipelines[@]}; do
  for model in ${models[@]}; do
    echo "Running $pipeline with $model model with API Diff"
    WITHOUT_APIDIFF=False python benchmark.py -n with_diff -m $model -p $pipeline
    git add . && git commit -m "[Benchmark] update results" && git push
  done
done
