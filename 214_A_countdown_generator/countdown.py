"""
Bite 214. A countdown generator
"""


def countdown():
    """Write a generator that counts from 100 to 1"""
    for i in reversed(range(1, 101)):
        yield i
