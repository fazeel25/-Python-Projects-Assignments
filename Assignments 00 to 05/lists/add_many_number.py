# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    
    return total

def main():
    number_list = [1,2,4,56,78,4]
    result = sum(number_list)
    print(result)

if __name__ == '__main__':
    main()



