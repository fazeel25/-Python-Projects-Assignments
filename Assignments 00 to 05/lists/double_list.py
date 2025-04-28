"""
Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]
"""


def main():
    number_list = [1,2,3,4]

    for i in range(len(number_list)):
        number_list[i] = number_list[i] * 2
    print(number_list)

if __name__ == '__main__':
    main()