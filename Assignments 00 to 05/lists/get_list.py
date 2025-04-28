"""
Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
"""

def main():
    lst = []
    while True:
        val = input("Enter a value: ")
        if not val == "":
            lst.append(val)
        else:
            print(f"Here's the list: {lst}")
            break

if __name__ == "__main__":
    main()