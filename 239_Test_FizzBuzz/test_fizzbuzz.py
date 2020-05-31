from fizzbuzz import fizzbuzz
import pytest

# write one or more pytest functions below, they need to start with test_


@pytest.mark.parametrize(
    "test_input,expected", [
        (3, 'Fizz'),
        (18, 'Fizz'),
        (54, 'Fizz'),
        (99, 'Fizz'),
        (5, 'Buzz'),
        (25, 'Buzz'),
        (35, 'Buzz'),
        (55, 'Buzz'),
        (15, 'Fizz Buzz'),
        (60, 'Fizz Buzz'),
        (90, 'Fizz Buzz'),
        (360, 'Fizz Buzz'),
        (8, 8),
        (67, 67),
        (1001, 1001),
        (1234, 1234),
        pytest.param(33, 'Buzz', marks=pytest.mark.xfail),
        pytest.param(50, 'Fizz', marks=pytest.mark.xfail),
        pytest.param(150, 150, marks=pytest.mark.xfail),
    ],
)
def test_fizzbuzz(test_input, expected):
    assert fizzbuzz(test_input) == expected
