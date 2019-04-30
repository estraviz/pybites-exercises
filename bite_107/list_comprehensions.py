"""Bite 107. Filter numbers with a list comprehension
"""


def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    return [number for number in numbers if is_positive(number) and is_even(number)]


def is_positive(num):
    return num > 0


def is_even(num):
    return num % 2 == 0
