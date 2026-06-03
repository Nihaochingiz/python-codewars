# https://www.codewars.com/kata/5b047875de4c7f9af800011b/train/python

def sentence(lst):
    indexed_words = []

    for item in lst:
        for key, value in item.items():
            index = int(key)
            indexed_words.append((index, value))

    indexed_words.sort()

    result = []

    for index, word in indexed_words:
        result.append(word)

    return ' '.join(result)






List = [
        {'4': 'dog' }, {'2': 'took'}, {'3': 'his'},
        {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
       ]



print(string_reordering(List))