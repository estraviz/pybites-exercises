"""
Bite 278. Major and minor numbers
"""

from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    counter = Counter(numbers)
    major = counter.most_common(1)[0][0]
    minor = counter.most_common()[:-2:-1][0][0]
    return major, minor
