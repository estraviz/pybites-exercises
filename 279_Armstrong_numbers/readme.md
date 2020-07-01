# Bite 279. Armstrong numbers

## Description

In [number theory](https://en.wikipedia.org/wiki/Number_theory) there are many interesting numbers - eg. [Armstrong numbers](https://en.wikipedia.org/wiki/Narcissistic_number) numbers, [Happy numbers](https://en.wikipedia.org/wiki/Happy_number), [Meertens numbers](https://en.wikipedia.org/wiki/Meertens_number), just name a few.

In this bite, you will try to solve the _Armstrong number question_: given an integer, determine if it is an _armstrong number_.

An armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits. See [this reference](https://en.wikipedia.org/wiki/Narcissistic_number) for more info and here are some examples:

a) 153 is an armstrong number. It's a 3 digits number:

```python
    (1^3) + (5^3) + (3^3)= 153.
```

b) 371 is also an armstrong number.

c) any single digit numbers (1-9) are armstrong numbers as well.
