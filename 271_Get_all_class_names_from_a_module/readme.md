# Bite 271. Get all class names from a module

## Description

In this Bite you will write a function to get all the class names from the module passed in.

Only return the class names that start with an uppercase character.

We recommend you check out the `inspect` module for this.

Here is how your code should work:

```python
  >>> from cls import get_classes
  >>> import csv, string
  >>> get_classes(csv)
  ['Dialect', 'DictReader', 'DictWriter', 'Error', 'Sniffer', 'StringIO']
  >>> get_classes(string)
  ['Formatter', 'Template']
```

Introspection of Python can be very useful. Have fun!

**Note:** Python 3.8 is required for passing the tests for the `csv` module. BTW, I suggest using `pyenv` for managing different versions of Python ;)
