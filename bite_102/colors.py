'''
Bite 102. Infinite loop, input, continue and break
'''

VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        key = input("Introduce a color: ").lower()
        if key == "quit":
            print("bye")
            break
        elif key not in VALID_COLORS:
            print("Not a valid color")
        else:
            print(key)
