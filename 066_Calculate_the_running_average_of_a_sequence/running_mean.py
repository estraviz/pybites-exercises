"""
Bite 66. Calculate the running average of a sequence
"""


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    current = []
    for i, num in enumerate(sequence):
        current.append(
            round((sum(sequence[:i]) + num)/(len(sequence[:i]) + 1), 2))
    return current
