#!/usr/bin/env python3

import sys
import utils
import string

#The output list size is >= the input size

def get_phonekeys_numbers(): #Example: 1-800-468-2333 -> 1-800-GOT-BEEF
    varmapNumbers = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    varmap = varmapNumbers.copy() #phone number keypad letters

    for num, letterList in varmapNumbers.items():
        for letter in letterList:
            varmap[letter] = varmapNumbers[num]

    return varmapNumbers

def get_phonekeys():
    varmap = get_phonekeys_numbers()
    for key, val in varmap.copy().items():
        for letter in val: 
            letters = val.copy()
            letters.remove(letter)
            varmap[letter] = letters
    return varmap

def get_shiftkeys():
    varmap = {}
    for char in string.ascii_lowercase: 
        varmap[char] = [char, char.upper()]
        varmap[char.upper()] = [char, char.upper()]
    return varmap

def gen_variations(s: str, varmap: dict):
    print(s)
    variations = set([s])

    for i in range(len(s)):
        letter = s[i]
        if not (letter in varmap): continue
        letterVariations = []
            
        for subLetter in varmap[letter]:
            for variationStub in variations:
                variationStub = variationStub[:i] + subLetter + variationStub[(i+1):]
                letterVariations.append(variationStub)

        for variation in letterVariations:
            if not variation in variations:
                print(variation)
        variations.update(letterVariations)

    return variations

if __name__ == "__main__":
    flags, vals, mainArgs = utils.getFlags(sys.argv[1:])

    varmap = None
    if ('use' in vals):
        use = vals['use'].strip().lower()
        if (use == 'phonekeys'): varmap = get_phonekeys()
        elif (use == 'phonekey_numbers'): varmap = get_phonekeys_numbers()
        elif (use == 'shiftkeys'): varmap = get_shiftkeys()
        else: raise Exception("Valid maps are: ['shiftkeys', 'phonekeys', 'phonekey_numbers']")
    if varmap is None: varmap = get_shiftkeys()

    for word in mainArgs:
        gen_variations(word, varmap)
    if len(mainArgs) == 0:
        for word in sys.stdin:
            word = word.strip()
            if len(word) == 0: continue
            gen_variations(word, varmap)
