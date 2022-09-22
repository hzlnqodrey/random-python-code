#!/bin/bash

if test -n "$PATH"; then echo "Your path is not empty"; fi

# -n indicate which check if a string variable empty or not 
# [] is alias to test command, so this line below equivalent with line above

if [ -n "$PATH" ]; then echo "Your path is not empty"; fi