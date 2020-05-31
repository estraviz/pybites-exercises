from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_


def test_divide_by_three():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(18) == 'Fizz'
    assert fizzbuzz(54) == 'Fizz'
    assert fizzbuzz(99) == 'Fizz'


def test_divide_by_five():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(25) == 'Buzz'
    assert fizzbuzz(35) == 'Buzz'
    assert fizzbuzz(55) == 'Buzz'


def test_divide_by_fifteen():
    assert fizzbuzz(15) == 'Fizz Buzz'
    assert fizzbuzz(60) == 'Fizz Buzz'
    assert fizzbuzz(90) == 'Fizz Buzz'
    assert fizzbuzz(360) == 'Fizz Buzz'


def test_not_multiple_of_three_or_five():
    assert fizzbuzz(8) == 8
    assert fizzbuzz(67) == 67
    assert fizzbuzz(1001) == 1001
    assert fizzbuzz(1234) == 1234
