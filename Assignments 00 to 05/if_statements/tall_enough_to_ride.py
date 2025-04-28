"""
Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like
"""

requirement_height = 50
def main():
    while True:
        try:
            height = float(input("Enter your height "))
            if height >= requirement_height:
                print("You're tall enough to ride! ✅")
                break
            else:
                print("You're not tall enough to ride, but maybe next year! ❌")
        except ValueError:
            print("Enter valid number")

if __name__ == "__main__":
    main()