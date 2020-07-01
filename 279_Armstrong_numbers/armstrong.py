"""
Bite 279. Armstrong numbers
"""


def is_armstrong(n: int) -> bool:
    return sum([int(x)**len(str(n)) for x in str(n)]) == n
