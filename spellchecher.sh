#!/bin/bash

sed '
s/^[ \t]*//;s/[ \t]*$//
s/[^a-zA-Z0-9 ]//g
s/ /\
/g
' $1 | sed '/^$/ d' > out.txt


grep -i -v -Fx -f english.txt out.txt

rm out.txt
#grep -i -v -Fx -f english.txt out.txt



