
## String Permutation & Utilities

Example of how to guess a password of length 12 given the keyboard keys used are: {P, I, M, S, 1, 7}:

```
echo "pims127" | ./lenextender 12 | ./charpermute | ./orderpermute
```

Example of how to guess a 12 character password given the letter keys pressed on a phone keypad are: {1, 4, 6, 7}:

```
echo "1467" | ./lenextender 12 | ./charpermute phonekeys | ./charpermute | ./orderpermute
```