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



