"""
Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
"""

def get_last_element(lst):
    print(f"\nThe first value in your list is: {lst[-1]}")

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
        get_last_element(lst)
        

if __name__ == "__main__":
    main()
        