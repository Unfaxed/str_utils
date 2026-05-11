#!/usr/bin/env python3

import sys
import utils

def get_morse_map():
    return ({
        'a': '.- ',
        'b': '-... ',
        'c': '-.-. ',
        'd': '-.. ',
        'e': '. ',
        'f': '..-. ',
        'g': '--. ',
        'h': '.... ',
        'i': '.. ',
        'j': '.--- ',
        'k': '-.- ',
        'l': '.-.. ',
        'm': '-- ',
        'n': '-. ',
        'o': '--- ',
        'p': '.--. ',
        'q': '--.- ',
        'r': '.-. ',
        's': '... ',
        't': '- ',
        'u': '..- ',
        'v': '...- ',
        'w': '.-- ',
        'x': '-..- ',
        'y': '-.-- ',
        'z': '--.. ',
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
        '0': '----- ',
        '.': '.-.-.- ',
        '!': '.-.-.-- ',
        '?': '..--.. ',
        ',': '--..-- ',
        ' ': '/ ',
    }, True)

def get_reverse_morse_map():
    return ({
        '.-.-.- ': '.',
        '.-.-.-- ': '!',
        '..--.. ': '?',
        '--..-- ': ',',
        '.---- ': '1',
        '..--- ': '2',
        '...-- ': '3',
        '....- ': '4',
        '..... ': '5',
        '-.... ': '6',
        '--... ': '7',
        '---.. ': '8',
        '----. ': '9',
        '----- ': '0',
        '-... ': 'b',
        '...- ': 'v',
        '.... ': 'h',
        '-.-. ': 'c',
        '..-. ': 'f',
        '.--- ': 'j',
        '-..- ': 'x',
        '-.-- ': 'y',
        '--.. ': 'z',
        '.-.. ': 'l',
        '.--. ': 'p',
        '--.- ': 'q',
        '.-- ': 'w',
        '-.. ': 'd',
        '--. ': 'g',
        '.-. ': 'r',
        '... ': 's',
        '-.- ': 'k',
        '--- ': 'o',
        '..- ': 'u',
        '.- ': 'a',
        '.. ': 'i',
        '-- ': 'm',
        '-. ': 'n',
        '. ': 'e',
        '- ': 't',
        '/ ': ' ',
    }, False)

def map_word(word, varmap, single_char_mapping = True):
    out = ''
    word = word.lower().strip()

    if (single_char_mapping): #keys of varmap are all one character long
        for i in range(len(word)):
            letter = word[i]
            if (letter in varmap): out += varmap[letter]
            else: out += letter
    else:
        out = word + ' '
        for key in varmap: #TODO could make a huffman coding tree
            out = out.replace(key, varmap[key])

    out = out.strip()
    return out.strip()
        

if __name__ == "__main__":
    flags, vals, mainArgs = utils.getFlags(sys.argv[1:])

    varmap = None
    single_char_mapping = True
    if ('use' in vals):
        use = vals['use'].strip().lower()
        if (use == 'morse'): varmap, single_char_mapping = get_morse_map()
        elif (use == 'reverse_morse' or use == 'revmorse' or use == 'demorse'): varmap, single_char_mapping = get_reverse_morse_map()
        else: raise Exception("Valid mappings are: ['morse', 'reverse_morse]")
    if varmap is None: 
        varmap, single_char_mapping = get_morse_map()

    for word in mainArgs:
        print(map_word(word, varmap, single_char_mapping=single_char_mapping))
    if len(mainArgs) == 0:
        for word in sys.stdin:
            word = word.strip()
            if len(word) == 0: continue
            print(map_word(word, varmap, single_char_mapping=single_char_mapping))