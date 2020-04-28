"""
Bite 225. Swap case PyBites characters
"""

PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    return ''.join(char.swapcase() if char.lower() in PYBITES else char
                   for char in text)
