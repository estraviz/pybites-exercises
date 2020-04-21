import string

import pandas as pd

import series as se


def test_basic_series():
    ser = se.basic_series()
    assert isinstance(ser, pd.Series)
    assert ser.name == "Fred"
    assert ser.dtype == "int64"
    assert all(n in [1, 2, 3, 4, 5] for n in ser.values)


def test_floats_series():
    ser = se.float_series()
    assert isinstance(ser, pd.Series)
    assert ser.dtype == "float64"
    assert len(ser) == 1001
    assert ser.sum() == 500.5


def test_alpha_index_series():
    ser = se.alpha_index_series()
    assert isinstance(ser, pd.Series)
    assert ser.dtype == "int64"
    assert len(ser) == 26
    assert sum(ser.values) == 351
    assert all(c in string.ascii_lowercase for c in ser.index)


def test_object_values_series():
    ser = se.object_values_series()
    assert isinstance(ser, pd.Series)
    assert len(ser) == 26
    assert all(c in string.ascii_uppercase for c in ser.values)
    assert ser[101] == "A"
    assert ser[126] == "Z"
