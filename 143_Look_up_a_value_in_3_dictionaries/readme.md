# Bite 143. Look up a value in 3 dictionaries

## Description

In this Bite you are presented with 3 dictionaries. Complete `get_person_age` that takes a `name` as argument and returns the age if in any of the 3 dictionaries. The lookup should be case insensitive, so _tim_, _Tim_ and _tiM_ should all yield _30_. If not in any of the dictionaries, return `Not found`.

Note that some persons are in 2 of the 3 dictionaries. In that case return the age of the last dictionaries (so `group3` takes precedence over `group2` and `group2` takes precedence over `group1`). Check out the standard library ... :) - have fun!
