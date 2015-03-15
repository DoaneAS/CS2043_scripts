#! /bin/bash

IFS=$\n

titles=()
# populate the array using a while loop and process substitution (direct piping will not work)
while read line1
do
titles+=("$line1")
done < <(curl -s https://web.archive.org/web/20140301052344/http://www.movies.com/rss-feeds/top-ten-box-office-rss | grep "title" | sed 's/<title><!\[CDATA\[//;s/\]\]><\/title>//')

descriptions=()
# populate the array using a while loop and process substitution (direct piping will not work)
while read line2
do
descriptions+=("$line2")
done < <(curl -s https://web.archive.org/web/20140301052344/http://www.movies.com/rss-feeds/top-ten-box-office-rss | grep "description" | sed 's/<description><!\[CDATA\[//;s/\]\]><\/description>//')

export x=1
export y=0

#echo first title
#echo "${titles[$((x+1))]}"
#echo "${descriptions[$((y+1))]}"
#echo
#echo fifth title
#echo "${titles[$((x+5))]}"
#echo
#echo all titles
#for title in "${titles[@]}"
#do
#echo "$title"
#done
#echo all descriptions
#for description in "${descriptions[@]}"
#do
#echo "$description"
#done

number=1
while [ $number -ge 1 ]
do
 clear
 for title in "${titles[@]}"
 do
 echo "$title"
 done
 if [ $number -ge 11 ]
 then
  number=0
 else
  echo -n "Choose a movie (1-10) >"
  read number
  if [ $number -ge 1 ]
  then
   clear
  fi
  echo Movie "$((number))"  
  echo Synopsis
  echo
  echo "${descriptions[$((y+number))]}"
  echo
  echo Press enter to return
  read index
 fi
done
