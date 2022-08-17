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
center_msg "Welcome to Artifact download Script"
sleep 2

which wget 1>/dev/null 2>/dev/null

if [ $? -ne 0 ]
then
        center_msg  "Please install wget and come back later"
        exit 1
	sleep 2
fi

if [ -e "artifact.json" ]
then
        center_msg "Removing old artifact.json file."
        rm -rf artifact.json
	sleep 2
fi

if [ -e "bootcamp-node-project-1.0.0.tgz" ]
then
        center_msg "Removing old artifact file."
        rm -rf boot*
        sleep 2
fi


curl -u local:12345 -X GET 'http://165.22.229.234:8081/service/rest/v1/components?repository=npm-repository&sort=version' | jq "." > artifact.json


artifactDownloadUrl=$(jq '.items[].assets[].downloadUrl' artifact.json --raw-output)

wget --http-user=local --http-password=12345 $artifactDownloadUrl

sleep 3

tar zxvf bootcamp-node-project-1.0.0.tgz

sleep 2

center_msg "changing to  directory called package"
cd package

sleep 1

center_msg "installing dependencies"
npm install

sleep 3

center_msg "running the application background"
cd app
node server.js &

center_msg "End of script"

