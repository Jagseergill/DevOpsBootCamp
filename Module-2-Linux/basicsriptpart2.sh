#!/bin/bash
echo " Reading a prompt from user input"
read -p "Enter your password: " input
echo "Your password is : $input"

echo "--------------------------------"
echo "--------Next part---------------"

echo "All Parameters $*"
echo "Number of parameters $#"
echo "testing: $@"

echo "User $1"
echo "Group $2"

echo "----------------------"
echo "------For Loop--------"

for parameter in $*
do
	if [ -d "$parameter" ]
	then
		echo "Executing Script in the $parameter folder"
		ls -l "$parameter"
	fi
	echo $parameter
done

echo "====================="
echo "-----While Loop starting----------"

sum=0
while true
do
	read -p "Enter the score: " score
	if [ "$score" == "q" ]
	then
		break
	fi
	sum=$(($score + $sum))
	echo "Total Score: $sum"
done

echo "------------------------"
echo "-----Funtion executing---"

game_score() {
 sum=0
 while true
 do
        read -p "Enter the score: " score
        if [ "$score" == "q" ]
        then
                break
        fi
        sum=$(($score + $sum))
        echo "Total Score: $sum"
 done
}

game_score
echo "---------------------"
echo "----Funtion by passing parameter------"
file_creation(){
	file_name=$1
	is_shell_script=$2
	touch $file_name
	echo "File $file_name is created "

	if [ "$is_shell_script" = true ]
	then
		chmod u+x $file_name
		echo "Execution permission added"
	fi
}

file_creation testing.txt
file_creation nextlevelscript true


echo "------------------------"
echo "-----Return a value in function-----"

sum() {
	total=$(($1+$2))
	return $total
}
sum 2 10 
result=$?
echo "Sum of two number is: $result"


