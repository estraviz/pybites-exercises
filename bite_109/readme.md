# Bite 109. Workout dict lookups and raising an exception

In this Bite you learn how to lookup values from a dictionary or in Python: `dict`.

You are presented with `workout_schedule` with keys: days and values: workouts. Complete `get_workout_motd` that receives a day string, title case it so the function can receive case insensitive days, look it up in the dict and do two things:

If the day (key) is not in the dictionary, raise a `KeyError`, we don't want this function to continue, the caller needs to catch this exception,
If the key is in the dictionary, return `chill` or `go_train` depending if it's a Rest day or not. The latter you will need to string-interpolate using `format`.
