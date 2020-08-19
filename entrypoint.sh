#!/bin/sh -l

#very generic setup. We would normally update this with our requirements. We will keep the generic Hello World.

echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"