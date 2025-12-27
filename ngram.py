#!/usr/bin/env python3

import sys
import utils

def load_ngrams(fileName, N):
    ngrams = set()

    file = open(fileName, 'r')

    for line in file.readlines():
        line = line.strip().lower()
        if (len(line) < N or "'" in line): continue
        for i in range(len(line) - N + 1):
            ngrams.add(line[i:(i+N)])

    file.close()

    return ngrams

def count_ngrams(word, ngrams, N):
    ngramCount = 0
    for i in range(len(word) - N + 1):
        ngram = word[i:(i+N)]
        if ngram in ngrams: ngramCount += 1
    return ngramCount

def rank_ngrams(words, ngrams, showCount=False, threshold=0):
    if len(ngrams) == 0: raise Exception("ngrams set is empty")
    first_item = next(iter(ngrams))
    N = len(first_item) #assuming all same length

    ngram_ranking = {}
    for word in words:
        ngram_ranking[word] = count_ngrams(word, ngrams, N)

    sorted_ranking = sorted(words, key=lambda i: -ngram_ranking[i])

    for word in sorted_ranking:
        if (ngram_ranking[word] < threshold): continue
        if showCount: print("%s: %s" % (word, ngram_ranking[word]))
        else: print(word)

if __name__ == "__main__":
    flags, vals, mainArgs = utils.getFlags(sys.argv[1:])
    fileName = vals['file'] if ('file' in vals) else "/usr/share/dict/words"

    N = 3
    passedWords = mainArgs
    if len(mainArgs) > 0:
        try:
            N = int(mainArgs[0])
            passedWords = mainArgs[1:]
        except: pass

    if N < 1: raise Exception("N must be at least 1")

    showCount = ('c' in flags) or ('show-count' in flags)
    doSort = not (('k' in flags) or ('no-sort' in flags) or ('skip-sort' in flags)) #implies showCount

    threshold = 0
    if ('min' in vals):
        try:
            threshold = int(vals['min'])
        except: 
            raise Exception("Could not parse --min parameter")

    ngrams = load_ngrams(fileName=fileName, N=N)

    if (doSort):
        words = set()
        for word in passedWords: words.add(word.strip().lower())
        if len(words) == 0:
            for word in sys.stdin: words.add(word.strip().lower())

        rank_ngrams(words, ngrams, showCount=showCount, threshold=threshold)
    else:
        words = passedWords if len(passedWords) > 0 else sys.stdin
        for word in words: 
            word = word.strip().lower()
            count = count_ngrams(word, ngrams, N)
            if (count >= threshold): print("%s: %s" % (word, count))

