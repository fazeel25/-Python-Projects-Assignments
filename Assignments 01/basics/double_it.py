# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

max_val = 100

def main():
    try:
        curr_val = int(input("Enter a number"))
        while curr_val < max_val:
            curr_val = curr_val * 2
            print(curr_val)
            
    except ValueError:
        print("Enter a valid input!")
        
if __name__ == '__main__':
    main()