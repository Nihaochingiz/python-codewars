# https://www.codewars.com/kata/580755730b5a77650500010c/train/python

def sort_my_string(s):
    even_string = ''
    odd_string = ''

    if len(s) < 8:
        return

    for  index, char in enumerate(s):
        if index % 2 == 0:
            even_string += char
        elif index % 2 == 1:
            odd_string += char
    return f'{even_string} {odd_string}'


print(sort_my_string("CodeWars"))