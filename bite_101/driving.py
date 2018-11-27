'''
Bite 101. f-strings and a simple if/else
'''

MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print name is allowed / not allowed to drive based on MIN_DRIVING_AGE"""
    if age >= MIN_DRIVING_AGE:
        print(f"{name} is allowed to drive".replace("\xa0", " "))
    else:
        print(f"{name} is not allowed to drive".replace("\xa0", " "))
