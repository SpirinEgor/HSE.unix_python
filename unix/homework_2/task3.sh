#!/bin/bash

sed -E 's/\ *(#include)(\ *")(.*)"/#include <\3>/g' "$1" |
  sed -E 's/".*"/""/g' |
  sed -E '/\/\*/,/\*\//d' |
  sed -E '/\ *\/\//d' |
  grep -E "^\ *(#include).*" |
  sed -E 's/\ *(#include)(\ *<)(.*)>/\3/g' |
  sed -E 's/\.h//g'
