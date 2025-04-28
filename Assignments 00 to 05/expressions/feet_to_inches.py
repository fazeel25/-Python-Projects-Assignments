"""
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
"""

inches_in_feet: int = 12

def main():

    feet:float = float(input("Enter a value in feet "))
    inches:float = feet * inches_in_feet 
    print("That is", inches, "inches!")

if __name__ == '__main__':
    main()
