"""
Bite 208. Find the number pairs summing up N
"""


def find_number_pairs(numbers, N=10):
    output = []
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i != j and sum_N(x, y, N) and (y, x) not in output:
                output.append((x, y))
    return output


def sum_N(a, b, N):
    return a + b == N
