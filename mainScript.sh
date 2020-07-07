#!/bin/bash

./runTest.sh
if [ $? -eq 0 ]; then
    ./runFizzBuzz.sh
fi