#!/bin/bash

cd pythonScripts

python3 dbCreator.py > /dev/null 2>&1 &
echo "Creating the DB"

