#!/usr/bin/env bash

head -c "$(shuf -i 0-"$((2**16-1))" -n 1)" /dev/random > rnd.txt
