#!/bin/bash

print_header(){
	printf  "\e[32m#%0.s\e[0m" $(seq 1 $(tput cols))
	printf "\n"
}
center_msg(){
	msg=$1
	terminalcols=$(tput cols)
	msg_len=(echo ${#1})
	pre_space=$(($((terminalcols-msg_len))/2))
	print_header
	printf " %0.s" $(seq 1 $pre_space)
	printf "\e[31m%s\e[31m" "$1"
	printf "\n"
	print_header

}

check_remotepassword(){
	if [ ! -e remotepass ]
	then
		center_msg "please store your password in >> remotepass <<file and retry"
		exit 1
	fi
}
check_remoteuserfile(){
	if [ ! -e remoteuser ]
        then
                center_msg "please store your user file  in >> remoteuser <<file and retry"
                exit 1
        fi

}
check_listofserversfile(){
	if [ ! -e list_of_server ]
        then
                center_msg "please store your list of servers  in >> list_of_server <<file and retry"
                exit 1
        fi

}
center_msg "Welcome to Inventory Script"
check_remotepassword
check_remoteuserfile
check_listofserversfile

ssh_opt="sshpass -f remotepass ssh -n -o StrictHostKeyChecking=No -o PubkeyAuthentication=No jagseer"

while read server
do
	echo "Working on $server"
	os_type=$($ssh_opt@$server "cat /etc/os-release" | grep -w "NAME" | awk -F "NAME=" '{print $2 }' | tr '"' ' ')
	echo $os_type | grep -i "ubuntu" 1>/dev/null 2>&1
	if [ $? -eq 0 ]
	then
		os_version=$($ssh_opt@$server "cat /etc/os-release" | grep "VERSION_ID"| awk -F "VERSION_ID=" '{print $2}'|  tr '"' " " )
	else
		os_version=$($ssh_opt@$server "cat /etc/redhat-release" | awk -F "release" '{print $2}')
	fi

	echo "OS type is : $os_type"
	echo "OS version is : $os_version"	

	sleep 3

done < list_of_server


center_msg "Thank you for using this shell script"
