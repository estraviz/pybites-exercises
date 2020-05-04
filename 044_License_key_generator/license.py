"""
Bite 44. License key generator
"""

from secrets import token_hex


def gen_key(parts=4, chars_per_part=8):
    return '-'.join(token_hex(chars_per_part//2) for _ in range(parts)).upper()
