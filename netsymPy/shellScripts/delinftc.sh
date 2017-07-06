#!/bin/bash
PROG_TC=`which tc`
$PROG_TC qdisc del dev $1 root
