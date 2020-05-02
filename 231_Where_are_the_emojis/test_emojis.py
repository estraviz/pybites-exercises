import pytest

from emojis import get_emoji_indices


@pytest.mark.parametrize("emojis, expected", [
    ('We 💜 Python 🐍', [3, 12]),
    ('We are so happy 😊😍 seeing you all coding', [16, 17]),
    ('😂 ROFL that is funny 😂', [0, 21]),
    ('No way 😭, that is not cool 🤔', [7, 27]),
    ('Great job 👌 hitting that Ninja 💪 belt', [10, 31]),
    ('Good luck with your 100 days of code 💯', [37]),
    ('Our 🥋 ninjas are on fire 🔥', [4, 25]),
    ('Happy Valentine 💕, buy some gifts 🎁', [16, 34]),
    ('pytest is so cool 😎, after grasping it 🤯', [18, 39]),
    ('Books can be boring 😴, better to code 💪❗', [20, 38, 39]),
])
def test_get_emoji_indices(emojis, expected):
    assert get_emoji_indices(emojis) == expected
