"""
Bite 257. Extract users dict from a multiline string
"""

import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    dic = {}
    for line in passwd.split('\n')[1:-1]:
        fields = line.split(':')
        user = fields[0]
        name = 'unknown' if not fields[4] else re.sub(
            r"\,+", ' ', fields[4].rstrip(','))
        dic[user] = name
    return dic
