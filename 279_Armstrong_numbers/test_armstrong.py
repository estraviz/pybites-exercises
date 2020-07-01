import pytest

from armstrong import is_armstrong


@pytest.mark.parametrize('number, expected', [
    (5, True),  (153, True), (370, True),
    (371, True),  (4150, False), (2020, False),
    (9474, True), (1989, False), (11, False),
])
def test_armstrong(number, expected):
    assert is_armstrong(number) == expected
