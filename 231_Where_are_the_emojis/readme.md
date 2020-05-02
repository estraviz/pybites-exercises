# Bite 231. Where are the emojis

## Description

In this Bite you are given a `list` of strings that contain emojis. Complete `get_emoji_indices` returning a list of indices of the emojis found in the text.

Here is an example how it should work:

```python
>>> from emojis import get_emoji_indices
>>> text = "We see more and more 🐍 Python 🥋 ninjas, keep it up 💪"
>>> text.index('🐍')
21
>>> text.index('🥋')
30
>>> text.index('💪')
51
>>> get_emoji_indices(text)
[21, 30, 51]
```

Have fun and keep calm and code in Python!
