#!/bin/bash
PROG_IF=`which ifconfig`
$PROG_IF -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'
# the output will generated with ":" at the end