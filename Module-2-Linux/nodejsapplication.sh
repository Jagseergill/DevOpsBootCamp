#!/bin/bash
sudo apt update

echo "install node, npm, curl, wget, net-tools"
sudo apt install -y nodejs npm curl net-tools
sleep 15
echo ""
echo "##################################"
echo ""

echo -n "Set log directory location for the application (absolute path): "
read LOG_DIRECTORY

if [ -d $LOG_DIRECTORY ]
then
	echo " $LOG_DIRECTORY already exist"
else
	mkdir -p $LOG_DIRECTORY
	echo "A new directory $LOG_DIRECTORY is created"
fi


cd $LOG_DIRECTORY

npm_version=$(npm --version)
echo " NPM $npm_version version installed."

node_version=$(node --version)
echo " NPM $node_version version installed."

echo ""
echo "###################################"
echo ""

wget https://node-envvars-artifact.s3.eu-west-2.amazonaws.com/bootcamp-node-envvars-project-1.0.0.tgz

tar zxvf ./bootcamp-node-envvars-project-1.0.0.tgz

export APP_ENV=dev
export DB_PWD=mysecret
export DB_USER=myuser


cd package

npm install

node server.js &


ps aux | grep node | grep -v grep


netstat -ltnp | grep :3000

