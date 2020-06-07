"""
Bite 222. Split an iterable in groups of size n
"""

import types
from itertools import islice


def group(iterable, n):
    """Splits an iterable set into groups of size n and a group
       of the remaining elements if needed.

       Args:
         iterable (list): The list whose elements are to be split into
                          groups of size n.
         n (int): The number of elements per group.

       Returns:
         list: The list of groups of size n,
               where each group is a list of n elements.
    """
    if not isinstance(iterable, types.GeneratorType):
        generator = (element for element in iterable)
    else:
        generator = iterable

    output = []
    while True:
        chunk = list(islice(generator, n))
        if chunk:
            output.append(chunk)
        else:
            break
    return output


if __name__ == '__main__':
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    ret = group(iterable, n)
    print(ret)
