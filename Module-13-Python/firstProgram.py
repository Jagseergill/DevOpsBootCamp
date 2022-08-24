print('Hello World')
print("There are 20 days have " + str(45) + " minutes. ")
print(f"20 days have {20 * 24 * 60} minutes")

# Variable usability
calculation_minutes = 24 * 60
name = "minutes"
print(f"There are 20 days have {calculation_minutes} {name}")


# function

def days_of_units():
    print(f"There are 20 days have {calculation_minutes} {name} by using function.")
    print("All Good!")


days_of_units()


# Function with parameters:

def days_calculation(num_days, customer_msg):
    print(f"There are {num_days} days have {num_days*calculation_minutes} {name} by using function.")
    print(customer_msg)


days_calculation(34, "Thank you!")
days_calculation(46, "Great!")
