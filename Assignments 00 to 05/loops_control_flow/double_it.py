# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    while True:
        for i in range(100):
            num = input("Enter a number ")
            num = num * 2
            print(num)
            break

if __name__ == "__main__":
    main()