#!/bin/bash

sed -E '1d' "$1" |
  sed -E 's/(.*),(.*),(.*),(.*)/<tr><td>\1<\/td><td>\2<\/td><td>\3<\/td><td><a href=\"mailto:\4\">\4<\/a><\/td><\/tr>/g' |
  sed -E '1s/^/<html>\n<head><meta charset=\"utf-8\"><\/head><body>\n<table>\n/' |
  sed -E '$s/$/\n<\/table>\n<\/body>\n<\/html>/'
