"""
Bite 54. Nicer formatting of a poem or text
"""

INDENTS = 4


def print_hanging_indents(poem):
    lets_indent = False
    for line in poem.split('\n'):
        if line == '':
            lets_indent = False
        else:
            if lets_indent:
                print(' '*INDENTS + line.lstrip())
            else:
                print(line.lstrip())
            lets_indent = True
