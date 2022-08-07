#!/bin/bash

echo -n "Would you like to sort the processes output by memory or CPU? (m/c) "
read sortby
echo -n "How many results do you want to display? "
read lines

if [ "$sortby" = "m" ]
then
	echo "-----Processes are sorted by memory based------"
	 ps aux --sort -%mem | grep -i `whoami` | head -n "$lines"
 elif [ "$sortby" = "c" ]
 then
	 echo"----Processes are sorted by cpu based---------"
	  ps aux --sort -%cpu | grep -i `whoami` | head -n "$lines"
  else
	  echo "No input provider or you have enter wrong information"
fi

