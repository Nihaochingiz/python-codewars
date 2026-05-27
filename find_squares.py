# https://www.codewars.com/kata/60908bc1d5811f0025474291/train/python

def find_squares(num):
    first_square = (num // 2 + 1)**2
    second_square = (num // 2)**2

    return f'{first_square}-{second_square}'

print(find_squares(9))
print(find_squares(5))
print(find_squares(7))




