# Guess the Number Game Python Project (computer)

import random

def guess(y):
    random_number = random.randint(1,y)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {y} "))
        if guess > random_number:
            print("your guess is high try again")
        elif guess < random_number:
            print("your guess is low try again")

    print("Congrates you win")

if __name__ == "__main__":
    guess(10)