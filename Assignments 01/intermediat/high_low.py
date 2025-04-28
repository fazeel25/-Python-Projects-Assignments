"""
We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

You make a guess, saying your number is either higher than or lower than the computer's number

If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

These steps make up one round of the game. The game is over after all rounds have been played.
"""
import random

def main():
    ROUNDS = 5
    score = 0
    print("Welcome to the High-Low Game!")
    print("-----------------------------")
    while ROUNDS:
        computer_guess = random.randint(1,100)
        try:
            user_guess = int(input("Enter your guess number "))

            if not (1 <= user_guess <= 100):
                print("Please enter a number between 1 and 100!")
                continue

            think = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
            if think not in ["higher", "lower"]:
                print("Invalid choice! Please enter 'higher' or 'lower'.")
                continue 
            
            if (user_guess > computer_guess and think == "higher") or (user_guess < computer_guess and think == "lower"):
                print(f"You were right! The computer's number was {computer_guess}")
                score += 1
                print(score)
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_guess}")
                print(score)

            ROUNDS -= 1

        except ValueError:
            print("Invalid input number!")

    print(f"Game Over! Your final score is: {score}/{ROUNDS}")

    if score == ROUNDS:
        print("Wow! You played perfectly!")
    elif score > ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()