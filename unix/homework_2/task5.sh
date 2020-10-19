#!/bin/bash

man "${@:2}" | sed -E "/^$1/,/^[A-Z]/!d" | sed -E 's/^ *//g' | head -n -2
