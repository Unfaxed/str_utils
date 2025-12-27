
## String Permutation & Utilities

**charpermute.py**: Uses a mapping for a character to a list of alternative characters to try. Given an input word, all possible combinations of substitutions are printed to stdout. By default, prints all combinations of upper- and lower-case substitutions, such as "abc" -> "Abc", "ABc", "aBc", ...

**lenextender.py**: Given a target length (first argument) and input words (piped or as first argument), guesses all possible combinations of letters to duplicate, in order, to extend the string to the target length. For example, "abc" to length 4 produces "aabc", "abbc", and "abcc"

**ngram.py**: Given a file passed in after `--file` argument (by default, uses `/usr/share/dict/words`), and a value for N (by default 3, first argument), extracts all N-grams out of the word file, then sorts each input word by how many N-grams it contains.

Additional parameters:
- `-c`/`--show-count`: Show the number of n-grams each word contains in the output
- `-k`/`--no-sort`: Do not sort the output, and only count the number of n-grams in each input word (implies `-c`)

**orderpermute.py**: Lists all permutations of the characters passed in as input

<hr>

### Example 1: Guess a word of length 5 given the letters used are: {Z, A, P, I}:

```
echo "zapi" | ./lenextender.py 5 | ./orderpermute.py | ./ngram.py 4 --min 2
```

Explanation: First, make random guesses to extend the word to 5 characters, such as "zzapi", "zaapi", etc. Next, list all permutations, such as "zazip", "zaipz", etc. Finally, filter out the results that have less than two 4-grams. The word "pizza" should be in the final list.

### Example 2: Guess words that were typed given the numbers used in a phone keypad

```
echo "7625" | ./charpermute.py --use phonekey_numbers | ./ngram.py 3 --min 2
```

Explanation: If the keys pressed on an old flip-phone were 7, 6, 2, and 5, given the keypad mappings, the possible words include "rock", "soak", and "sock"