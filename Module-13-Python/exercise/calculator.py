def calculate(number1, number2, operation):
    if operation == "plus":
        print(number1 + number2)
    elif operation == "minus":
        print(number1 - number2)
    elif operation == "multiply":
        print(number1 * number2)
    elif operation == "divide":
        print(number1 / number2)


number_of_calculation_done = 0

while True:
    number1 = input("Please enter the first number: ")

    if number1 == "exit":
        print("Exiting the program.")
        print(f"you did {number_of_calculation_done} calculation.")
        break

    number2 = input("please enter the second number: ")

    operation = input("What operation do you want to perform on these number (plus, minus, multiply, divide):")

    valid_number = number1.isnumeric() and number2.isnumeric()
    valid_operation = operation == "plus" or operation == "minus" or operation == "multiply" or operation == "divide"

    if not valid_number:
        print("Please enter only number")
    elif not valid_operation:
        print("Please enter a valid operation in the list. This one is not supported")
    else:
        calculate(int(number1), int(number2), operation)
        number_of_calculation_done += 1
