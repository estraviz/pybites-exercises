"""
Bite 189. Filter a list of names
"""

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    count = 0
    for name in names:
        if count == MAX_NAMES or name.startswith(QUIT_CHAR):
            break
        if name.startswith(IGNORE_CHAR) or any(char.isdigit() for char in name):
            continue
        count += 1
        yield name
