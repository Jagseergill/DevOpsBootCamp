employees = [{
    "name": "Tina",
    "age": 30,
    "birthday": "1990-03-10",
    "job": "DevOps Engineer",
    "address": {
        "city": "New York",
        "country": "USA"
    }
},
    {
        "name": "Tim",
        "age": 35,
        "birthday": "1985-02-21",
        "job": "Developer",
        "address": {
            "city": "Sydney",
            "country": "Australia"
        }
    }]


# Write a function that accepts a list of dictionaries with employee age
# and prints out the name and age of the youngest employee


def print_employee_info(employees):
    youngest_employee_age = employees[0]['age']
    youngest_employee_name = employees[0]['name']

    for employee in employees:
        if employee['age'] < youngest_employee_age:
            youngest_employee_name = employee['name']
            youngest_employee_age = employees['age']
    print(f"Name of the youngest employee is :{youngest_employee_name}")
    print(f"Name of the youngest employee age is: {youngest_employee_age}")


print_employee_info(employees)


# Write a function that accepts a string and calculates the number of upper case letters and lower case letters
print("----------------------------------")


def count_upper_and_lower_char(string):
    lower_count = 0
    upper_count = 0
    for char in list(string):
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    print(f"Number of lower case letter: ", lower_count)
    print(f"Number is upper case letter: ", upper_count)


count_upper_and_lower_char("sWWbb137WATbfgdbWb")

# Write a function that prints the even numbers from a provided list
print("----------------------------------")


def print_even_number(number_list):
    for number in number_list:
        if number % 2 == 0:
            print(number)


print_even_number([0, 3, 9, 10, 2, 13, 120])
