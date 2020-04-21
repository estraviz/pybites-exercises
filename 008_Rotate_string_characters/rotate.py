"""Bite 8. Rotate string characters
"""


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    return string[n:] + string[:n]
