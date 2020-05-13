"""
Bite 115. Count leading spaces
"""

from itertools import takewhile


def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return sum(1 for _ in list(takewhile(lambda x: x == ' ', text)))


def another_solution(text):
    count = 0
    for char in text:
        if char == ' ':
            count += 1
        else:
            break
    return count
