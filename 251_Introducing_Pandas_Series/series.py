"""
Bite 251. Introducing Pandas Series
"""

import string

import pandas as pd


def basic_series() -> pd.Series:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    return pd.Series([1, 2, 3, 4, 5], name='Fred')


def float_series() -> pd.Series:
    """Create a pandas Series containing the all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    return pd.Series([x/1000 for x in range(1001)])


def alpha_index_series() -> pd.Series:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    return pd.Series(list(range(1, 27)), index=[chr(x) for x in range(97, 123)])


class MyClass:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


def object_values_series() -> pd.Series:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    list_of_objects = [MyClass(chr(i)) for i in range(65, 91)]
    b = MyClass('B')
    print(type(b))
    return pd.Series([x.name for x in list_of_objects], index=list(range(101, 127)))
