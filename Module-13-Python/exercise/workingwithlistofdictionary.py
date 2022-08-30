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

# Print out - the name, job and city of each employee using a loop.
# The program must work for any number of employees in the list, not just 2

for employee in employees:
    print(f"Employee name is: {employee['name']}")
    print(f"Employee job is: {employee['job']}")
    print(f"Employee address is: {employee['address']['city']}")
    print("----------------------------------------")

country = employees[1]['address']['country']
print(f"Country of second employee is : {country}")
