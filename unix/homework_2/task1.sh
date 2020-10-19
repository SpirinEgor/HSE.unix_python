#!/bin/bash

grep -Ps "^[A-Z]([A-Za-z]|\d)*\s+([a-z]|m_)([A-Za-z]|\d)*\_?\;$" <<< "$1"
