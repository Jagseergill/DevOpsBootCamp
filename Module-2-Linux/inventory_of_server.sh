#!/bin/bash
Server_name=$(uname -n)
IP_Address=$(ifconfig | grep -i inet | awk 'NR==2 {print $2}')
os_type=$(uname)
uptime=$(uptime | awk '{print $3}' | tr -d ',')

echo -e "The Server name is : $Server_name    \nIP Address is : $IP_Address \nOS type is : $os_type \nUptime for server is : $uptime"
