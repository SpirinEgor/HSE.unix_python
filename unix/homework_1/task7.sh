#!/usr/bin/env bash

if [[ "$(uname -s)" == "Darwin" ]]; then
	gfind /etc/ -type f -name "*.conf" -printf "%f\n\0" | sort -z | tr "\n\0" "\0\n" | head -n 10 | tr "\0\n" "\n\0"
else
	find /etc/ -type f -name "*.conf" -printf "%f\n\0" | sort -z | tr "\n\0" "\0\n" | head -n 10 | tr "\0\n" "\n\0"
fi

