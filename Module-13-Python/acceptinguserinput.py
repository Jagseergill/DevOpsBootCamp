calculation_to_units = 24
name_of_unit = "hours"


def days_calculation(num_days):
    return (f"There are {num_days} days have {num_days * calculation_to_units} "
            f"{name_of_unit} by using function.")


user_input = input("Hey User enter the number of day\n")
user_input_number = int(user_input)

calculated_value = days_calculation(user_input_number)
print(calculated_value)
