# Guess My Number

import random

def main():
    secret_number = random.randint(0,99)
    print("I am thinking of a number between 0 and 99...")
    print()
    while True:
        try:
            user_guess = int(input("Enter a guess "))
            if user_guess == secret_number:
                print(f"Congrats! The number was: {secret_number}")
                break
            elif user_guess > secret_number:
                print("Your guess is too high")
            elif user_guess < secret_number:
                print("Your guess is too low")

        except ValueError:
            print("please enter a valid number ")

if __name__ == '__main__':
    main()