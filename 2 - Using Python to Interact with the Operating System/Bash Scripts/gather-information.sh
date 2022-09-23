#!/bin/bash
line="======================================="
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime # cmd
echo $line # empty lines

echo "FREE"
free # cmd
echo $line # empty lines

echo "WHO"
who  # cmd
echo $line # empty lines

echo "Finishing at $(date)"