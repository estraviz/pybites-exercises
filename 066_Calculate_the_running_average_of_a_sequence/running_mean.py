"""
Bite 66. Calculate the running average of a sequence
"""

from itertools import accumulate


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    for i, num in enumerate(accumulate(sequence)):
        yield round(num/(i + 1), 2)
