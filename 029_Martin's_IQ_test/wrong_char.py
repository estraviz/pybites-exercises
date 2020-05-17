"""
Bite 29. Martin's IQ test
"""


def get_index_different_char(chars):
    alpha, non_alpha = set(), set()
    for i, char in enumerate(chars):
        if str.isalnum(str(char)):
            alpha.add(i)
        else:
            non_alpha.add(i)
    return next(iter(alpha)) if len(alpha) == 1 else next(iter(non_alpha))
