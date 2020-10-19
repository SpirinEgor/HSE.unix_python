#!/usr/bin/env bash

if [[ "$(uname -s)" == "Darwin" ]]; then
  gfind . -maxdepth 1 -type f -name "*.txt" -user "$(whoami)" -printf "%i\n" | wc -l
else
  find . -maxdepth 1 -type f -name "*.txt" -user "$(whoami)" -printf "%i\n" | wc -l
fi
