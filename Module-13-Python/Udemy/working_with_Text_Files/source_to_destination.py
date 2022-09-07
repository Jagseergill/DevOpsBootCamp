source_file = "random.txt"
destination_file = "new_random.txt"

source_file_object = open(source_file, 'r')
content = source_file_object.read()
source_file_object.close()

destination_file_object = open(destination_file, 'w')
destination_file_object.write(content)
destination_file_object.close()
