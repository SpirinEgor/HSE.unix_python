#!/usr/bin/env bash

INPUT_FILE="data"
OUTPUT_FILE="data"
head -c -0 "$INPUT_FILE" >> "$OUTPUT_FILE"
