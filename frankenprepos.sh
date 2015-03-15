#!/bin/bash
# script to select lines, remove punctuation and blank lines, sub  new line for space
#count word frequency and write top 10 words with freq to file

sed '
s/\.//g
s/\,//g
s/[^a-zA-Z0-9 ]//g
/^$/ d
s/ /\
/g
' "frankenstein.txt" | sed '/^$/ d' > out.txt

 fgrep -v -f prepositions.txt out.txt | sort | uniq -ic | sort -nr | head -100 > frankenprepos.txt

rm out.txt
cat frankenprepos.txt