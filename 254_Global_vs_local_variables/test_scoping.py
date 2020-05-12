import pytest

from scoping import sum_numbers


@pytest.mark.parametrize("arg, ret, hundreds_value", [
    ([], 0, -1),
    ([1, 2, 3], 6, -1),
    ([40, 50, 60], 150, 0),
    ([140, 50, 60], 250, 2),
    ([140, 150, 160], 450, 6),
    ([1140, 150, 160], 1450, 20),
])
def test_sum_numbers(arg, ret, hundreds_value):
    assert sum_numbers(arg) == ret
    from scoping import num_hundreds
    assert num_hundreds == hundreds_value
