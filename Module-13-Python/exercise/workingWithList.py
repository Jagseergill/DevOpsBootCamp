my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]

for num in my_list:
    if num < 10:
        print(num)

# Instead of printing the elements one by one, make a new list that has all
# the elements higher than or equal 10 from this list in it and print out this new list.

num_list = []

for num_list_two in my_list:
    if num_list_two >= 10:
        num_list.append(num_list_two)
print(num_list)

# Ask the user for a number as input and print a list that
# contains only those elements from my_list that are higher than the number given by the user.


user_input = input("Enter a number: ")
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
my_new_list = []
for number in my_list:
    if number > int(user_input):
        my_new_list.append(number)
print(my_new_list)

