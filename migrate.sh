#!/bin/bash

find ./results/benchmark -name 'report.json' -exec bash ./scripts/run_migrations.sh {} \;

