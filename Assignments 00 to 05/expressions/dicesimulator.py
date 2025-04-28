"""
Simulate rolling two dice, three times.
Prints the results of each die roll. 
This program is used to show how variable scope works.

"""
import random

num_dies = 6

def roll_dies():

    dies1:int = random.randint(1,num_dies)
    dies2:int = random.randint(1,num_dies)
    total:int = dies1 + dies2
    print("Total of two dies", total)

def main():
    dies1:int = 10
    print("die1 in main() starts as: " + str(dies1))
    roll_dies()
    roll_dies()
    roll_dies()
    print("die1 in main() starts as: " + str(dies1))

if __name__ == "__main__":
    main()

