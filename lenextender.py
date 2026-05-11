#!/usr/bin/env python3

import sys
import math
import utils

def allocate_slots(n, k):
    #All ways to allocate k items to n slots with no zeros
    #Example: n=2, k=5: [(3, 2), (1, 4), (2, 3), (4, 1)]
    if (n <= 0): return []
    if (n == 1): return [(k,)]

    results = []
    sums = get_sums(k)

    for sum in sums:
        if len(sum) == n:
            results.append(sum)
    return results

def get_sums(n):
    #Ex. for n=3, returns {(1, 2), (1, 1, 1), (3,), (2, 1)}. Not considering sums as commutative here because sum order is needed later
    sumData = {1: [1]}

    for i in range(2, n+1):
        sums = set([(i,)])
        for j in range(1, i):
            sums.add((i-j, j))
            if (i-j > 1):
                for subSum in sumData[i-j]:
                    subSumCopy = list(subSum)
                    subSumCopy.append(j)
                    sums.add(tuple(subSumCopy))
            if (j > 1):
                for subSum in sumData[j]:
                    subSumCopy = list(subSum)
                    subSumCopy.insert(0, i-j)
                    sums.add(tuple(subSumCopy))
        sumData[i] = sums
    
    return sumData[n]


def gen_extended_length(x: str, newLen: int, verbose: bool = True):
    if (len(x) >= newLen): return [x]
    else:
        results = set()
        for allocation in allocate_slots(len(x), newLen):
            result = ''
            contains_zero = False
            for i, val in enumerate(allocation):
                if (val == 0): 
                    contains_zero = True
                    break
                result += x[i]*val
            if (contains_zero): continue
            if (verbose): print(result)
            results.add(result)
        return results

if __name__ == "__main__":
    flags, vals, mainArgs = utils.getFlags(sys.argv[1:])

    strLen = -1
    if (len(mainArgs) > 0):
        try: strLen = int(sys.argv[1])
        except: pass
    if (strLen == -1): raise Exception("Must pass in a value for output length as first argument")
    
    words = mainArgs[1:] if len(mainArgs) > 1 else sys.stdin

    for word in words:
        word = word.strip()
        gen_extended_length(word, math.ceil(len(word)*1.2) if strLen == -1 else strLen)