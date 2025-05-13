import random

def guess_number():
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100!")
    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

guess_number()