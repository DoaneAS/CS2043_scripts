#!/bin/bash
wget -O- "http://www.cs.cornell.edu/courses/cs2043/2015sp/assignments/superbowl.html" |
sed '
s/<[^>]*>//g
s/\W//
s/[\#\}\{\$].*//
s/^[ \t]*//
/^$/ d' > superbowl_text.txt
#just need to deifine as interactive va
NAFTER=$2
NBEFORE=$1
awk '{for (i=1;i<=NF;i++) print $i }' superbowl_text.txt > superbowl_word.txt

#grep 'Pat.*' -A $NBEFORE -B $NAFTER superbowl_word.txt

#grep 'Seahawk.*' -A $NBEFORE -B $NAFTER superbowl_word.txt

grep -w 'Pat.*\|Seahawk.*' -A $NBEFORE -B $NAFTER superbowl_word.txt  > teamwords.txt


cat teamwords.txt