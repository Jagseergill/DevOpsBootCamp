#!/bin/bash
echo "########Setup and Configure Server############"
file_name=config.yaml

config_dir=$1

if [ -d "$config_dir" ]
then
	echo "Reading config directory contects"
        config_files=$(ls "$config_dir")
else
	echo "$config_dir not found and creating one...."
	mkdir "$config_dir"
	touch "$config_dir/config.sh"
fi
echo "--------------------------------"


user_group=$2

if [ "$user_group" == "jagseer" ]
then
	echo "Configuring Server with Jagseer Group"
elif [ "$user_group" == "admin" ]
then
	echo "Configuring server with Admin Group"
else
	echo "No permission to configer anything"
fi


echo "##################################"
echo "-----------Scripting end----------"



echo "using file $file_name to configure something"
echo "Here are all configuration files: $config_files" 
