# https://www.codewars.com/kata/563700da1ac8be8f1e0000dc/train/python

def max_redigit(num):
    if not isinstance(num, int) or num < 100 or num > 999:
        return -1

    lst_num = [int(x) for x in str(num)]
    sorted_lst_num = sorted(lst_num, reverse=True)
    sorted_int = int(''.join(map(str, sorted_lst_num)))
    return sorted_int


print(max_redigit(123))