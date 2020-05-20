# Bite 214. A countdown generator

## Description

Write a simple generator that counts from 100 to 1. It can just return the `int`s one by one, no fancy formatting, just focus on the basic mechanics of generators. Remember that going beyond `1` it would trigger a `StopIteration` exception.

Here is how it works:

```python
>>> from countdown import countdown
>>> cd = countdown()
>>> next(cd)
100
>>> next(cd)
99
>>> next(cd)
98
>>> next(cd)
97
...
... 95 calls more
...
>>> next(cd)
1
>>> next(cd)
Traceback (most recent call last):
  File "", line 1, in 
StopIteration
```

Good luck, have fun and keep it Python!
