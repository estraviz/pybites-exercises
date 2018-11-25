'''
Bite 1. Sum n numbers
'''

def sum_numbers(numbers=None):
    if numbers is None:
        return sum(range(1,101))
    return sum(numbers)
