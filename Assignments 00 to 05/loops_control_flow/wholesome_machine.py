# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

correct_affirmation = "I am capable of doing anything I put my mind to."

def main():
    while True:
        print(f"Please type the following affirmation: {correct_affirmation} ")
        user_input = input()

        if user_input == correct_affirmation:
            print("That's right! :)")
            break 
        else:
            print("Hmmm That was not the affirmation. Please try again.")

if __name__ == "__main__":
    main()