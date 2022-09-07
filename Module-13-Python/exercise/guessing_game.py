from random import randint

while True:
    number_to_guess = randint(1, 19)
    user_guess = input("Guess the number:")
    if user_guess == "exit":
        print("Exiting the game.")
        break

    user_num = user_guess.isnumeric()

    if user_num == number_to_guess:
        print("You won!!!")
    elif user_num < number_to_guess:
        print("You guessed too low!")
    elif user_num > number_to_guess:
        print("You guess too high!")

