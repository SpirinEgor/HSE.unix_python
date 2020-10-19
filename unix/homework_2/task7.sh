#!/bin/bash

SPREADSHEET_URL="https://docs.google.com/spreadsheets/d/1Gk-7b6NkWUu7KswpuXs7yQ8uqcBNQ10T6hffXBX8YnY/export?gid=0&format=csv"
NAME="Спирин Егор"
TIME_STEP=1

function get_score_by_name {
  score=$(curl "$1" -s -L | sed -E "/$2/!d" | sed -E "s/(.*),(.*),(.*).*/\3/")
  echo "$score"
}

start_score=$(get_score_by_name "$SPREADSHEET_URL" "$NAME")
while true; do
  current_score=$(get_score_by_name "$SPREADSHEET_URL" "$NAME")
  if [[ "$current_score" != "$start_score" ]]; then
    exit 0
  fi
  sleep $TIME_STEP
done
