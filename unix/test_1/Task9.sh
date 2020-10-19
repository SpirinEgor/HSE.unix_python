#!/bin/bash

INPUT_FILE=$1
OUTPUT_FILE=$1
echo "$(base64 "$INPUT_FILE")" > "$OUTPUT_FILE"
