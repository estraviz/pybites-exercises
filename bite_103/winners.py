'''
Bite 103. Loop through a dictionary and pluralise a word
'''

games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won=games_won):
    """Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""
    for k, v in games_won.items():
        msg = f"{k} has won {v} game"
        if v != 1:
            msg += "s"
        print(msg)
