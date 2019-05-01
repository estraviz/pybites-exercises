"""Bite 153. Round a sequence of numbers
"""
import math


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    output = []
    for item in transactions:
        output.append(math.ceil(item) if up else math.floor(item))
    return output
