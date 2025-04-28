# Simulate rolling two dice, and prints results of each roll as well as the total.

import random
num_dies = 6

def roll_dies():

    die1:int = random.randint(1,num_dies)
    die2:int = random.randint(1,num_dies)
    total:int = die1 + die2
    print("Total of two dies", total)

    print("Dice have", num_dies, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


if __name__ == '__main__':
    roll_dies()