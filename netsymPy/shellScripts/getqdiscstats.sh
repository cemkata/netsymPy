#!/bin/bash
PROG_TC=`which tc`
$PROG_TC -p qdisc show dev $1
