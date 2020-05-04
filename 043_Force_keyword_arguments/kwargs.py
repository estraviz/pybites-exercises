"""
Bite 43. Force keyword arguments
"""


def get_profile(**kwargs):
    for key in kwargs:
        if key not in ['name', 'profession']:
            raise TypeError
    return f"{kwargs.get('name', 'julian')} is a {kwargs.get('profession', 'programmer')}"
