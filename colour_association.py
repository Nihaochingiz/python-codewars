# https://www.codewars.com/kata/56d6b7e43e8186c228000637/train/python

def colour_association(arr):
    result = []

    for pair in arr:
        result.append({pair[0]: pair[1]})
    return result


print(colour_association([["white", "goodness"]]))