# Bite 209. Write a Sphinx docstring

## Description

Your team uses `Sphinx` and wants you to comply with its standards for `docstring`s. As per the [Sphinx-RTD-Tutorial](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) a typical `Sphinx` docstring has the following format:

```python
"""[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
```

Based on this format and using the literal strings in italics below, write a docstring for `sum_numbers` that:

* has _Sums numbers_ for the _Summary_ part,
* receives _numbers: a list of numbers_ (type: `list`),
* raises a _TypeError: if not all numeric values passed in_,
* and returns _sum of numbers_ (type: `int`)

There's no need to implement the function (leave the `pass` in) as this is about writing the proper `docstring`.

**Note:** We will be adding annotations to this function in the next Bite so you will need to complete this Bite to unlock the next.
