#!/bin/bash
which wget 1>/dev/null 2>/dev/null

if [ $? -ne 0 ]
then
        echo "Please install wget and come back later"
        exit 1
fi
# It is used to removed the already index file exist in the directory 
if [ -e "index.html" ]
then
        echo "Removing old html files"
        rm -rf index.html
fi

# it is sued to get a git files from website
url="https://mirrors.edge.kernel.org/pub/software/scm/git/"
wget $url
if [ $? -ne 0 ]
then
        echo "unable to download the file from $url"
        exit 2
fi
declare -a git_vers
while read line 
do
        git_vers+=($(echo $line | sed -n '/git-\([0-9]\+\.\)\+tar.gz/p' | awk -F '"' '{print $2}' | cut -c 5- |awk -F '.tar.gz' '{ print $1 }'))

done < index.html

echo "The all avialbale git versions are:"
cnt=0
no_vers=${#git_vers[*]}
WIDTH=14


  for each_ver in ${git_vers[*]}

do
printf "%-*s %-*s %-*s %-*s %-*s %-*s %-*s %-*s\n" $WIDTH  ${git_vers[$cnt]}  $WIDTH ${git_vers[$((cnt+1))]} $WIDTH ${git_vers[$((cnt+2))]} $WIDTH ${git_vers[$((cnt+3))]} $WIDTH  ${git_vers[$((cnt+4))]} $WIDTH  ${git_vers[$((cnt+5))]}  $WIDTH  ${git_vers[$((cnt+6))]} $WIDTH  ${git_vers[$((cnt+7))]}

cnt=$((cnt+8))
if [ $cnt -ge $no_vers ]
 then
     break
fi
done

