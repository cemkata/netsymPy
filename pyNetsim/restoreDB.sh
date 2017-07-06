#!/bin/bash
echo "Cheking root"
if [ `id -u` = 0 ]; then
   echo "Root OK"
else
   echo "You are not root OK"
   exit 0
fi

cd pythonScripts

echo "Stoping the service"
pkill -f netsymPy.py

echo "Compacting DB"
python3 dbRestore.py

#echo "Starting service"
#python3 netsymPy.py &
