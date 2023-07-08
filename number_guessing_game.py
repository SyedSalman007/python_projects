import random

# value = 10
#
#
# def fun():
#     global value
#     value += 10
#     print(value)
#
#
# # value = 10
# fun()
# value = 10     this will give error


def number_guessing():
    print("Welcome to Number Guessing Game:")
    print("I am guessing a number between 1 and 100")
    check = input("Choose a difficulty level. Type 'easy' or 'hard': ")

    chosen = random.randint(1, 100)
    if check.lower() == "easy":
        choice = 10
    else:
        choice = 5

    while choice != 0:
        print(f"You have {choice} attempts remaining to guess the number:")
        guess = int(input("Make a guess: "))

        if guess == chosen:
            print(f"You got it the answer is {guess}")
            return
        elif guess > chosen:
            print("Too high")
        else:
            print("Too low")
        print("Guess again")
        choice -= 1
    print("You have run out of guesses, you lose")


number_guessing()
