"""
Bite 74. What day of the week were you born on?
"""

import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }.get(calendar.weekday(date.year, date.month, date.day))
