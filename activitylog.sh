#!/bin/bash

awk '
BEGIN {
    FS = ","
}
    ($2 ~ /run/){
            t1=$3
            getline
            tt=$3 - t1
            act["run"]+=tt}
    ($2 ~ /work/){
            tw=$3
            getline
            tt=$3 - tw
            act["work"]+=tt}
    ($2 ~ /farm/){
            tf=$3
            getline
            tt=$3 - tf
            act["farm"]+=tt}
END { print "run:", act["run"], "hrs",
"work:", act["work"], "hrs",
"farmers market:", act["farm"], "hrs"
}' activity_log.csv > activitylog.txt

cat activitylog.txt