"""
Bite 37. Rewrite a for loop using recursion
"""


def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    if start >= 1:
        print(start)
        return countdown_recursive(start - 1)
    print('time is up')
