#!/usr/bin/env bash

xargs -n1 ping -c 1 -W 1 < ip.txt > res.txt 2> err.txt

