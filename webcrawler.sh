#!/bin/bash

#download to stout, process then save

wget -O- "http://www.cs.cornell.edu/courses/cs2043/2015sp/assignments/superbowl.html" |
sed '
s/<[^>]*>//g
s/\W//
s/[\#\}\{\$].*//
s/^[ \t]*//
/^$/ d' > superbowl_text.txt

cat superbowl_text.txt