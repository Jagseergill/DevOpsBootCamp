calculation_to_units = 24
name_of_unit = "hours"


def days_calculation(num_days):
    if num_days > 0:
        return (f"There are {num_days} days have {num_days * calculation_to_units} "
                f"{name_of_unit} by using function.")


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_calculation(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered 0. Please enter more than 0.")
        else:
            print("You have entered a negative number.")
    except ValueError:
        print("Your input is not a digit. Please enter a valid digit.")


user_input = ""
while user_input != "exit":
    user_input = input("Hey User enter the number of day\n")
    validate_and_execute()
