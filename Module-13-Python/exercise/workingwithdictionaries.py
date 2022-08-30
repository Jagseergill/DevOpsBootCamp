employee = {"name": "Tim", "age": 30, "birthday": "1990-03-10", "job": "DevOps Engineer"}

# Updates the job to Software Engineer
employee["job"] = "Software Engineer"
print(employee)

# Remove the age key from the dictionary

employee.pop("age")
print(employee)

# Loop through the dictionary and print the key:value pairs one by one


for key, value in employee.items():
    print(f"{key}:{value}")

# Merge these two Python dictionaries into 1 new dictionary
dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

dict_merge = dict_one.copy()
dict_merge.update(dict_two)

print(dict_merge)

# Sums up all the values in the new dictionary and print it out
dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

dict_merge = dict_one.copy()
dict_merge.update(dict_two)

sum_of_values = 0

for value in dict_merge.values():
    sum_of_values = sum_of_values + value

print(sum_of_values)

# Prints the max and minimum values of the dictionary

dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

dict_merge = dict_one.copy()
dict_merge.update(dict_two)

merged_value = []

for value in dict_merge.values():
    merged_value.append(value)

merged_value.sort()

print(f"Min value: {merged_value[0]}")
print(f"Maximum value: {merged_value[len(merged_value)-1]}")
