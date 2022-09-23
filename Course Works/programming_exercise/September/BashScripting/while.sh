#!/bin/bash

n=10

while [ $n -ge 5 ]; do
    echo "Iteration $n"
    ((n-=1))
done
