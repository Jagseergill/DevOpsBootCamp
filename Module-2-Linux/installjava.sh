#!/bin/bash
sudo apt update
sudo apt install -y default-jre

java_version=$(java -version 2>&1 >/dev/null | grep "version" | awk '{print substr($3,2,2)}')
java_versionbycuttr=$(java -version 2>&1 >/dev/null | grep -i version | cut -d ' ' -f 3 | tr -d '"' | cut -d '.' -f 1)

if [ $java_version -ge 11 ]
then
	echo "Java version 11 or greater installed successfully"
else
	echo "Java installation failed" 
fi


