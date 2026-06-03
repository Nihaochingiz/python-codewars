# https://www.codewars.com/kata/593b1909e68ff627c9000186/train/python

def nickname_generator(name):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(name) < 4:
        return "Error: Name too short"
    if name[2] in vowels:
        return name[0:4]
    else:
        return name[0:3]

print(nickname_generator("Robert"))
print(nickname_generator("Jeannie"))
print(nickname_generator("Douglas"))
print(nickname_generator("Gregory"))
print(nickname_generator("Gregory"))