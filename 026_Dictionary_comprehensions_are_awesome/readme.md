# Bite 26. Dictionary comprehensions are awesome

A _dictionary comprehension_ is like a list comprehension, but it constructs a `dict` instead of a list. They are convenient to quickly operate on each (`key`, `value`) pair of a `dict`. And often in one line of code, maybe two after checking **PEP8** ;)

We think they are elegant, that's why we want you to know about them!

In this Bite you are given a dict and a set. Write a dictionary comprehension that filters out the items in the set and returns the resulting dict, so if your dict is `{1: 'bob', 2: 'julian', 3: 'tim'}` and your set is `{2, 3}`, the resulting dict would be `{1: 'bob'}`.

Check out the tests for more details. Have fun!
