"""
fileopen = open('sample_hash_input.txt', 'r')
# print(fileopen.mode)
# print(fileopen.readable())
print(fileopen.read())
fileopen.close()
"""
"""
fileopen = open('random.txt', 'w')
fileopen.write("This is a first line\n")
fileopen.write("This is a second line")
fileopen.close()
"""

"""
my_content = ["This is a data -1\n", "This is a data-2\n", "This is a data-3"]
fileopen = open('random.txt', 'w')
fileopen.writelines(my_content)
fileopen.close()
"""

my_content = ['This is using loop-iteratioin-1', 'This is using loop-iterantion-2', 'This is using loop-iteratioin-3']

file_object = open("with_loop.txt", 'a')

for each_lines in my_content:
    file_object.write(each_lines+"\n")
file_object.close()
