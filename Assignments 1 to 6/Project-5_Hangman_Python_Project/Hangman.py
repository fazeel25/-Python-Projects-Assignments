# Hangman Python Project

import random
from word import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)  
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)  
    used_letters = set()  
    lives = 10

    print("\n🎩 WELCOME TO HANGMAN 🎩")
    print(f"You have {lives} lives. Try to guess the word!\n")

    while len(word_letters) > 0 and lives > 0:
        
        print(f"📝 Used letters: {', '.join(used_letters)}")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("📌 Word: ", ' '.join(word_list))

        user_letter = input("\n🎯 Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter) 
            else:
                lives -= 1 
                print(f"❌ Incorrect! You have {lives} lives left.")

        elif user_letter in used_letters:
            print("⚠️ You have already used that letter. Try again!")
        else:
            print("🚫 Invalid character. Please enter a valid letter.")
        print("-" * 40)

    if lives == 0:
        print(f"\n💀 You lost! The word was **{word}**")
    else:
        print(f"\n🎉 Congratulations! You guessed the word **{word}** correctly!")


if __name__ == "__main__":
    hangman()