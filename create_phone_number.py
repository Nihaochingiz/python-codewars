# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):
    first_part = ''.join(map(str, n[0:3]))
    second_part = ''.join(map(str, n[3:6]))
    third_part = ''.join(map(str, n[6:10]))
    return f'({first_part}) {second_part}-{third_part}'



print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # -> "(123) 456-7890"