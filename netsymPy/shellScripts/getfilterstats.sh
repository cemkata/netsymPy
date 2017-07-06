#!/bin/bash
PROG_TC=`which tc`
$PROG_TC -p filter show dev $1
