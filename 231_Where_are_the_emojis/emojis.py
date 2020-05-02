"""
Bite 231. Where are the emojis?
"""

import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    return [index for index, char in enumerate(text) if re.match(IS_EMOJI, char)]
