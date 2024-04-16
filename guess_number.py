import random

top_range = input("Enter a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    # validate user input is a positive number
    if top_range <= 0:
        # Error message displayed if number is less than or equal to 0
        print("Please enter a number greater than 0 next time.")

        # quit the program
        quit()

    # generate random number using number entered by user
    random_number = random.randint(0, top_range)
else:
    print("Please enter a valid number next time.")

    # exit the program
    quit()

# create variable to keep track of number of guesses
num_of_guesses = 0

while True:
    # increment guesses
    num_of_guesses += 1

    # prompt user to guess the random number
    guess = input("Guess the number: ")

    # make sure what user enters is a number
    if guess.isdigit():
        guess = int(guess)

    # if it is not a number, then print error message
    else:
        print("Please enter a number next time.")
        continue

    if guess == random_number:
        print("Congratulations! You guessed the number! :)\n")

        # break out of loop once user has entered the correct guess
        break

    # help user narrow the random number down by letting them know if the guess is too high or too low
    elif guess > random_number:
        print("\nYour guess is too high!")
    else:
        print("\nYour guess is too low!")

# output the number of guesses it took
print("You got it in", num_of_guesses, "guesses!")




