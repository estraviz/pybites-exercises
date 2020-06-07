# Bite 222. Split an iterable in groups of size n

## Description

In this Bite you will complete the `group` function that receives an `iterable` and splits it up in n groups. Say we have a list of 10 `int`s and `n=3`, passing this into the function you'd get the following return:

```python
>>> iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n = 3
>>> from grouping import group
>>> group(iterable, n)
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
```

It should also work passing in a generator:

```python
>>> iterable = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> group(iterable, n)
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
```

And of course for different values for `iterable` and `n` (see also the tests):

```python
>>> iterable = [1, 2, 3, 4] * 3
>>> iterable
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> group(iterable, 2)
[[1, 2], [3, 4], [1, 2], [3, 4], [1, 2], [3, 4]]
```

Thanks to [Andrew (CodeItch)](https://codechalleng.es/profiles/CodeItch) for letting us know about this code/idea derived from one of [Sumo Logic's repos](https://github.com/SumoLogic).

Have fun and keep calm and code in Python! See you in the next Bite...
