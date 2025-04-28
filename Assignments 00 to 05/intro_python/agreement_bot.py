"""
Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" 
(the blank should be filled in with the user-inputted animal, of course).
"""


def favorite_animal():

    animal = input("Enter your favourite animal ")
    print(f"My favorite animal is also {animal}!")

if __name__ == '__main__':
    favorite_animal()
