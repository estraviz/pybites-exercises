# Bite 187. Actor/actress age at movie release

## Description

Ever wondered how old an actor/actress was in a particular movie? In this Bite you will write some code to find the answer.

Here is how it should work (the `Actor` and `Movie` `dataclasses` are provided):

```markdown
  (Pdb) actor
  Actor(name='Wesley Snipes', born='July 31, 1962')
  (Pdb) movie
  Movie(title='New Jack City', release_date='January 17, 1991')
  (Pdb) get_age(actor, movie)
  'Wesley Snipes was 28 years old when New Jack City came out.'
  ...
  (Pdb) actor
  Actor(name='Jennifer Aniston', born='February 11, 1969')
  (Pdb) movie
  Movie(title='Horrible Bosses', release_date='September 16, 2011')
  (Pdb) get_age(actor, movie)
  'Jennifer Aniston was 42 years old when Horrible Bosses came out.'
```

You might want to look into using `dateutil` to make this a lot easier :)

Keep calm and code in Python!
