# Guess the Number Game Python Project (user)

import random

def guess_the_number():
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 10, and I will try to guess it. 🤖")
    print("Tell me if my guess is too High (H), too Low (L), or Correct (C). Let's begin!\n")

    low = 1
    high = 10000
    feedback = ""

    while feedback != "c":
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low
        feedback = input(f"🤔 Is {computer_guess} too High (H), too Low (L), or Correct (C)? ").lower()
        
        if feedback == "h":
            high = computer_guess - 1
        elif feedback == "l":
            low = computer_guess + 1
        elif feedback == "c":
            print(f"\n🎉 Yay! I guessed your number {computer_guess} correctly!")
        else:
            print("⚠️ Please enter only H, L, or C.")

if __name__ == "__main__":
    guess_the_number()
