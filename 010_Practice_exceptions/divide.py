"""
Bite 10. Practice exceptionsGroup names by country
"""


def positive_divide(numerator, denominator):
    try:
        if numerator/denominator < 0:
            raise ValueError
        return numerator/denominator
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise
