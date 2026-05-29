# https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/python

def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    sum = 0
    for i in range(1, n + 1):
    # tn = n * (n + 1) * (n + 2) // 6
        sum = i * (i + 1) * (i + 2) // 6
    return sum

print(sum_triangular_numbers(4))
print(sum_triangular_numbers(5))

