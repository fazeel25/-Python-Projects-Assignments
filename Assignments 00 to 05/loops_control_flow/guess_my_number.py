# Guess My Number

import random

def main():
    random_number = random.randint(0,99)
    guess = int(input("Enter a guess "))
    while guess != random_number:
        if guess > random_number:
            print("Your guess is too high")
        if guess < random_number:
            print("Your guess is too low")
        print()
        guess = int(input("Enter a new guess "))

    print(f"Congrats! The number was: {random_number}")

if __name__ == "__main__":
    main()
