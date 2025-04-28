"""
Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

"""

def get_first_element(lst):
    print(f"\nThe first value in your list is: {lst[0]}")

def main():
    iterations = int(input("How many values do you want to enter? "))
    lst = []
    
    while iterations:
        val = input("Enter a value: ")
        if not val.strip():
            print("Invalid input. Please enter a non-empty value.")
            continue
        lst.append(val)
        iterations -= 1
    if iterations == 0:
        get_first_element(lst)
        

if __name__ == "__main__":
    main()
        


