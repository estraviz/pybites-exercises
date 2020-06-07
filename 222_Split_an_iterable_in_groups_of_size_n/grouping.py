"""
Bite 222. Split an iterable in groups of size n
"""


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
    full_list = []
    aux_list = []
    for i, num in enumerate(iterable):
        aux_list.append(num)
        if (i + 1) % n == 0:
            full_list.append(aux_list)
            aux_list = []
    if aux_list:
        full_list.append(aux_list)
    return full_list


if __name__ == '__main__':
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    ret = group(iterable, n)
    print(ret)
