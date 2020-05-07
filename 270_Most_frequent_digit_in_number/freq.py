"""
Bite 270. Most frequent digit in number
"""

from collections import Counter


def freq_digit(num: int) -> int:
    return int(Counter(list(str(num))).most_common(1)[0][0])
