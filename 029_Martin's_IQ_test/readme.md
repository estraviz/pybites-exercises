# Bite 29. Martin's IQ test

## Description

Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out which one of the given characters differs from the others. He observed that one char usually differs from the others in being _alphanumeric_ or not.

Please help Martin! To check his answers, he needs a program to find the _different_ one (the alphanumeric among non-alphanumerics or vice versa) among the given characters.

Complete `get_index_different_char` to meet this goal. It receives a `chars list` and returns an `int index` (zero-based).

Just to be clear, alphanumeric == `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`

### Examples

```python
['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
```

See the _TESTS_ tab for more details.
