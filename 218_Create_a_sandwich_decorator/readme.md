# Bite 218. Create a sandwich decorator

## Description

After creating our [Decorators and Context Managers learning path](https://codechalleng.es/bites/paths/decorators-context) we realized we did not have a _beginner_ decorator Bite, so here it is!

Complete the sandwich decorator which takes a function and prints _=== Upper bread slice ===_ (defined in `UPPER_SLICE`) and _=== Lower bread slice ===_ (defined in `LOWER_SLICE`) before and after calling the passed in function (`func`).

And voilà applying this decorator to `add_ingredients` you have your sandwich (see also the tests):

```python
>>> from sandwich import sandwich
>>> @sandwich
... def add_ingredients(ingredients):
...     print(' / '.join(ingredients))
...
>>> ingredients = ['bacon', 'lettuce', 'tomato']
>>> add_ingredients(ingredients)
=== Upper bread slice ===
bacon / lettuce / tomato
=== Lower bread slice ===
```

This is probably the easiest way to demo a decorator. Even so decorators can be confusing when you start using them so here is an article we wrote some time ago: [Learning Python Decorators by Example](https://pybit.es/decorators-by-example.html).
