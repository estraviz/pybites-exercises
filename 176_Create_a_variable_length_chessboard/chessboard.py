"""
Bite 176. Create a variable length chessboard
"""

WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for i in range(size):
        print((size//2)*(" #" if i % 2 == 0 else "# ") + '\n')
