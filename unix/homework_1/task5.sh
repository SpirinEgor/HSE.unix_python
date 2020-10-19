#!/usr/bin/env bash

if [[ "$(uname -s)" == "Darwin" ]]; then
	gfactor < "$1" > "$2"
else
	factor < "$1" > "$2"
fi

