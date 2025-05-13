import random
def guess_number():
    number = random.randint(1,100)
    print("Guess a number between 1 and 100")
    while True:
        guess = int(input("Enter your number:"))
        if guess < number:
            print("Too Low!Try Again!")
        elif guess > number :
            print("Too High! Try Again!")
        else:
            print("Congratulation!")
            break

guess_number()