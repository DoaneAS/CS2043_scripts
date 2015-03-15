#!/bin/bash
wget -O- "http://www.cs.cornell.edu/courses/cs2043/2015sp/assignments/superbowl.html" |
sed '
s/<[^>]*>//g
s/[\#\}\{\$].*//
s/^[ \t]*//
/^$/ d' > superbowl_text.txt

sed '
s/[^a-zA-Z0-9 ]//g
/^$/ d
s/ /\
/g
' "superbowl_text.txt" | sed '/^$/ d' | sort | uniq -ic | sort -nr | head -100 > commonwords.txt

cat commonwords.txt


