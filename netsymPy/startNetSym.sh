#!/bin/bash
echo "Cheking root"

if [ `id -u` = 0 ] ; then
   echo "Root OK"
else
   echo "You are not root OK"
   exit 0
fi

cd pythonScripts

echo "Starting service"
python3 netsymPy.py > /dev/null 2>&1 &
#python3 netsymPy.py &

