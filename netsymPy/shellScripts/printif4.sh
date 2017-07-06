#!/bin/bash
PROG_IF=`which ifconfig`
$PROG_IF | expand | cut -c1-8 | sort | uniq -u | awk -F: '{print $1;}'