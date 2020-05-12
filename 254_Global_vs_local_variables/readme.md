# Bite 254. Global vs local variables

## Description

This Bite is to illustrate scoping. You will sum numbers while keeping track of number of hundreds in a global variable called `num_hundreds`.

To illustrate this see this REPL output:

```python
>>> from scoping import sum_numbers, num_hundreds
>>> num_hundreds
-1
>>> sum_numbers([10, 20, 70])
100
>>> from scoping import num_hundreds
>>> num_hundreds
0
>>> sum_numbers([10, 120, 180])
310
>>> from scoping import num_hundreds
>>> num_hundreds
3
```

We planned to also illustrate `nonlocal`, but we will do that in a separate Bite ... Good luck and keep calm and code in Python!
