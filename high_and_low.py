# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    return f'{max(numbers)} {min(numbers)}'


print(high_and_low("1 2 3 4 5")) # return "5 1")