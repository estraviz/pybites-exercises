"""
Bite 117. Round a number even (a.k.a. banker's rounding)
"""

from decimal import Decimal


def round_even(number):
    """Takes a number and returns it rounded even"""
    return int(Decimal(number).to_integral_value())
