import typing

from annotations import sum_numbers


def test_sum_numbers():
    res = sum_numbers.__annotations__
    assert res.get('numbers') == typing.List[int]
    assert res.get('return') == int
