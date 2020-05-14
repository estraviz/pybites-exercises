"""
Bite 46. You are a programmer! Code Fizz Buzz
"""


def fizzbuzz(num):
    arr = []
    if num % 3 == 0:
        arr.append('Fizz')
    if num % 5 == 0:
        arr.append('Buzz')
    return ' '.join(arr) if arr else num
