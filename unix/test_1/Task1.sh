#!/bin/bash

EMAIL_REGEXP="^(\w|[\-\.\,])*[a-zA-Z](\w|[\-\.\,])*\@(\w+\.)*\w+$"
grep -Ps "$EMAIL_REGEXP"
