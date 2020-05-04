# Bite 44. License key generator

## Description

Write a function called `gen_key` that creates a license key with this format: _KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U_

The key consists of a combination of upper case letters and digits.

It takes two arguments: `parts` and `chars_per_part` which default to 4 and 8 respectively, so you can call the function like:

* `gen_key()` to get a similar key as above, or
* as `gen_key(parts=3, chars_per_part=4)` to get a shorter one, e.g. _54N8-I70K-2JZ7_

Before you default to `random`, check if _Python >= 3.6_ has a better option available for this task ...
