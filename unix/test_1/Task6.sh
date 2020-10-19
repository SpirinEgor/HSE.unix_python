#!/bin/bash

curl -s "$1" | sed -e "/<body.*\>/,/<\/body>/!d" | sed -e
