#!/bin/bash

# TEST
# -> a command that evaluates the conditions received and exits with zero when true, one when false

if test -n "$PATH"; then echo "Your path is not empty"; fi

# -n indicate which check if a string variable empty or not 
# [] is alias to test command, so this line below equivalent with line above

if [ -n "$PATH" ]; then echo "Your path is not empty"; fi