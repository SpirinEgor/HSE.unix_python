#!/bin/bash

BLOCK_LIST=$1

function is_url_blocked {
  url=$1
  true_host=$2
  true_scheme=$3

  true_host=$(echo "$true_host" | sed -E 's/(\.|\-|\/)/\\\1/g')

  checking_regexp="^($true_scheme\:\/\/)(.+\@)?(.+\.)*($true_host)(.)*$"
  [[ "$url" =~ $checking_regexp ]]
}

while read -r url; do
  result="ALLOW"
  while read -r host scheme; do
    if is_url_blocked "$url" "$host" "$scheme"; then
      result="DENY"
      break
    fi
  done < "$BLOCK_LIST"
  printf "%-100s%s\n" "$url" "$result"
done

