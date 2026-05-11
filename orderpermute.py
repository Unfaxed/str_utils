#!/usr/bin/env python3

#Must use all chars of input, only changes order

import math
import sys
import random
import utils

def uniq_permutations(n):
    permutations = []

    stack = [ ([], [i for i in range(n)]) ]
    while len(stack) > 0:
        usedArray, unusedSet = stack.pop(0)
        if len(usedArray) == n: permutations.append(usedArray)
        else:
            for nextIndex in unusedSet:
                newArray = usedArray.copy()
                newArray.append(nextIndex)
                newSet = unusedSet.copy()
                newSet.remove(nextIndex)
                stack.append((newArray, newSet))

    if (len(permutations) != math.factorial(n)): raise Exception("Did not generate permutation list correctly")
    return permutations

def rand_permute(n):
    choices = set([i for i in range(n)])
    permutation = []
    for i in range(n):
        choice = random.choice(tuple(choices))
        choices.remove(choice)
        permutation.append(choice)
    return permutation


def gen_permutations(x, prob=False, det=True, verbose=True):
    wordGen = lambda permutation: ''.join([x[i] for i in permutation])

    largeInput = len(x) >= 9
    if not det and not prob and largeInput: prob = True #problem grows O(n!), better for piping

    if (prob):
        generated = set()
        nTries = math.factorial(len(x))
        failThreshold = 0.01*nTries
        fails = 0
        for i in range(nTries):
            permutation = rand_permute(len(x))
            permWord = wordGen(permutation)
            if permWord in generated:
                fails += 1
                if (largeInput and fails >= failThreshold): break
            else:
                if (verbose): print(permWord)
                generated.add(permWord)
                fails = 0
    else:
        permutations = uniq_permutations(len(x))
        words = set([wordGen(permutation) for permutation in permutations])
        if verbose:
            for word in words: print(word)
        return words

if __name__ == "__main__":
    flags, vals, mainArgs = utils.getFlags(sys.argv[1:])

    prob = ('p' in flags) or ('prob' in flags) or ('probabilistic' in flags)
    det = ('d' in flags) or ('det' in flags) or ('deterministic' in flags)

    if len(mainArgs) == 0:
        for word in sys.stdin:
            word = word.strip()
            if len(word) == 0: continue
            gen_permutations(word, prob=prob, det=det)
    else:
        for word in mainArgs:
            gen_permutations(word.strip(), prob=prob, det=det)