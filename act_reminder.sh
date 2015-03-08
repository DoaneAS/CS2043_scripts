#!/bin/bash

# reading the date
export x=$(date | tr ' ' '\n' | grep 'Mon\|Tue\|Wed\|Thu\|Fri')
echo $x

awk 'BEGIN {FS=": "}
 toupper($1) ~ /$x/ {print $2}
END{}' myweekly_act.txt

