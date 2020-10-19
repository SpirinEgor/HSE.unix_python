#!/bin/bash

VK_USER_ID="id347745"
SPAN_ONLINE_REGEXP="<span class=\"pp_last_activity_text\">"
TIME_STEP=60

function get_status {
  url="https://vk.com/$1"
  status=$(curl "$url" -s -L | sed -E "/$SPAN_ONLINE_REGEXP/!d" | sed -E "s/\ *$SPAN_ONLINE_REGEXP//" | sed -E "s/( |<).*$//")
  echo "$status"
}

function send_message {
  echo -e "User with id \"$VK_USER_ID\" is now $1" | wall
}


user_status_step_ago=-1
while true; do
  user_status=$(get_status "$VK_USER_ID")
  if [[ "$user_status_step_ago" != "$user_status" ]]; then
    status="offline"
    if [[ $user_status == "Online" ]]; then
      status="online"
    fi
    send_message $status
  fi
  user_status_step_ago=$user_status
  sleep $TIME_STEP
done
