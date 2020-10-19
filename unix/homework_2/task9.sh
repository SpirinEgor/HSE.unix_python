#!/bin/bash

INPUT_FILE="Task9_ips.txt"

function get_city_by_ip {
  server="ipinfo.io"
  city=$(curl "$server/$1" -s | sed -E "/^ *\"city\"/!d" | sed -E "s/(^ *\"city\": \"|\",$)//g")
  echo "$city"
}
export -f get_city_by_ip

ips=()
while read -r ip; do
  ips+=("$ip")
done < "$INPUT_FILE"

parallel -k get_city_by_ip ::: "${ips[@]}"
