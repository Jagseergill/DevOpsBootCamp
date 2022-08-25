def days_calculation(num_days, conversion_unit):
    if conversion_unit == "hours":
        return f"There are {num_days} days have {num_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"There are {num_days} days have {num_days * 60} minutes"
    else:
        return "Unsupported units"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_calculation(user_input_number, days_and_unit_dictionary["Unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered 0. Please enter more than 0.")
        else:
            print("You have entered a negative number.")
    except ValueError:
        print("Your input is not a digit. Please enter a valid digit.")


user_input = ""
while user_input != "exit":
    user_input = input("Hey User enter the number of days with : unit\n")
    day_and_units = user_input.split(":")
    print(day_and_units)
    days_and_unit_dictionary = {"days": day_and_units[0], "Unit": day_and_units[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()
