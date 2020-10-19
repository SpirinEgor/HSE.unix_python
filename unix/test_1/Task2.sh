#!/bin/bash

HTML_REGEXP="(\<(?<TAG>\w+)\>).*(\<\/(?P=TAG)\>)"
SELF_CLOSING_REGEXP="\<\w+\/\>"
TAG_REGEXP="^($HTML_REGEXP|$SELF_CLOSING_REGEXP)$"
grep -Ps "$TAG_REGEXP"
