# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python

def stray(arr):
    stray_number = 0
    for num in arr:
        if arr.count(num) == 1:
            return num


