from time import *

f = open('C:\saol.txt')
lines = f.readlines()
f.close()

valid = []
match = []

for x in lines:
    x = x.strip()
    if len(x) >= 4 and len(x) <= 9:
        valid.append(x)

for x in valid:
    letters = ['h','c','f','h','ä','r','t','e','s']
    obligatorisk_bokstav = letters[4]

    temp_letters = letters
    bokstav_found = False
    found = 0
    
    chars = list(x)
    
    for y in chars:
        if y in obligatorisk_bokstav:
            bokstav_found = True
        
        if y in letters:
            used_letter = temp_letters.index(y)
            temp_letters.pop(used_letter) 
            found = found + 1

    if found == len(chars) and bokstav_found == True:
        chars = ''.join(chars)
        match.append(chars)

match = set(match)
