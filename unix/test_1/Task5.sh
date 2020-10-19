#!/bin/bash

EMAIL_REGEXP="(\w|[\-\.\,])*[a-zA-Z](\w|[\-\.\,])*\@(\w+\.)*\w+"

grep -Po "$EMAIL_REGEXP" < "$1" | sort | uniq -c | sort -nr | grep -Po "$EMAIL_REGEXP"
