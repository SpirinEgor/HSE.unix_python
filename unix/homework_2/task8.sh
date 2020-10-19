#!/bin/bash

MIN_LENGTH=6

function get_lcs {
  all_files=("$@")
  first_file="${all_files[0]}"
  for (( start=0; start<"${#first_file}"; ++start )); do
    for (( size=${#first_file} - start; size >= MIN_LENGTH; --size )); do
      lcs_candidate=$(echo "${first_file:start:size}" | sed -E 's/(\*|\[|\^|\||\(|\)|\ |\\|\.|\-)/\\\1/g')
      n_occurs=$(printf '%s\n' "${all_files[@]}" | grep -Pc "$lcs_candidate")
      if [[ "$n_occurs" -eq "${#all_files[*]}" ]]; then
        echo "$lcs_candidate"
        return 0
      fi
    done
  done
}

function get_filename {
  new_substr=" "
  if [[ "$1" =~ ^$2.* ]]; then
    new_substr=""
  fi
  echo "${1/"$2"/"$new_substr"}"
}

files=()
while read -r file; do
  files+=("$file")
done

lcs=$(get_lcs "${files[@]}")
if [ "$lcs" = "" ]; then
  exit 0;
fi

for file in "${files[@]}"; do
  new_filename=$(get_filename "$file" "$lcs")
  mv "$file" "$new_filename"
done
