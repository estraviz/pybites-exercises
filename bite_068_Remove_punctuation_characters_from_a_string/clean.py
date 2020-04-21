"""
Bite 68. Remove punctuation characters from a string
"""

import re


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return re.sub(r'[^\w\s]', '', input_string)
