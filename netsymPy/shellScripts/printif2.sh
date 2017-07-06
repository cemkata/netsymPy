#!/bin/bash
PROG_IP=`which ip`
$PROG_IP -o link show | awk -F': ' '{print $2}'