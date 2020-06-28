import pytest

from frequency import major_n_minor


@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3, 2, 2, 2, 3], (2, 1)),
    ([0, 0, 0, 1, 2, 2], (0, 1)),
    ([9, 8, 7, 8, 8, 9], (8, 7)),
    ([2, 0, 2, 0, 2, 1], (2, 1)),
    ([1, 3, 5, 7, 8, 8, 9, 9, 3, 5, 8, 7], (8, 1)),
    ([9, 0, 5, 7, 8, 8, 9, 0, 5, 9, 9, 5], (9, 7)),
])
def test_frequency(data, expected):
    assert major_n_minor(data) == expected
