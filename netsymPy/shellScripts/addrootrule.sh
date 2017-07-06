#!/bin/bash
PROG_TC=`which tc`
$PROG_TC qdisc add dev $1 handle 1: root htb