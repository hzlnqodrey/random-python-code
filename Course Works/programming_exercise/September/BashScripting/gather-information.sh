#!/bin/bash

line="---------------------------------------------"

echo "Starting at: $(date)"
echo $line

echo "UPTIME"
uptime # cmd
echo $line

echo "FREE"
free # cmd
echo $line

echo "WHO"
who  # cmd
echo $line

echo "Finishing at $(date)"
