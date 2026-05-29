# https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819/train/python

# objA = { 'a': 10, 'b': 20, 'c': 30 }
# objB = { 'a': 3, 'c': 6, 'd': 3 }
# combine(objA, objB) # Returns { a: 13, b: 20, c: 36, d: 3 }

def combine(*args):
    result = {}
    for arg in args:
        for key,value in arg.items():
            result[key] = result.get(key, 0) + value
    return result


# Пример 1: Два словаря
objA = {'a': 10, 'b': 20, 'c': 30}
objB = {'a': 3, 'c': 6, 'd': 3}
result1 = combine(objA, objB)
print(result1)  # {'a': 13, 'b': 20, 'c': 36, 'd': 3}

# Пример 2: Три словаря
dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}
dict3 = {'z': 5, 'w': 6}
result2 = combine(dict1, dict2, dict3)
print(result2)  # {'x': 1, 'y': 5, 'z': 9, 'w': 6}