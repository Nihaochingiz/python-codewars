def vowel_one(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_one = ''

    for c in s.lower():
        if c in vowels:
            vowel_one += '1'
        else:
            vowel_one += '0'
    return vowel_one

print(vowel_one("vowelOne")) # -> '01010101'