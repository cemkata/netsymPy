#!/bin/bash
if [ `id -u` = 0 ] ; then
    echo "root"
else
    echo "notroot"
fi