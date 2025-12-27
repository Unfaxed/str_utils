
## String Permutation & Utilities

Example of how to guess a word of length 5 given the letters used are: {Z, A, P, I}:

```
echo "zapi" | ./lenextender 5 | ./orderpermute | grep "pizza"
```

Example of how to guess a 12 character password given the letter keys pressed on a phone keypad are: {1, 4, 6, 7}:

```
echo "1467" | ./lenextender 12 | ./charpermute phonekeys | ./charpermute | ./orderpermute
```