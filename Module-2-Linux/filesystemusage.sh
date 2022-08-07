#!/bin/bash
df -Th | grep -vE "Filesystem|tmpfs|sr" | while read line
do
	file_system_name=$(echo $line | awk ' {print $1 }')
	file_system_usage=$(echo $line | awk ' {print $6}' | sed 's/%//g')

	echo "File system name is $file_system_name, it is using $file_system_usage"
	sleep 3

	if [ $file_system_usage -gt 40 ]
	then
		echo -e "Subject:Alert\n\n" | sendmail testmail@testmail.com
	fi

done
