"""
Bite 254. Global vs local variables
"""

num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    num_hundreds += sum(numbers)//100
    return sum(numbers)
