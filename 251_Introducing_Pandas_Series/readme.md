# Bite 251. Introducing Pandas Series

## Description

Let's get started with Pandas! In case you are not aware of who, or what, `pandas` is, [pandas](https://pandas.pydata.org/) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

The two primary data structures in `pandas` are the _**Series**_ and the _**DataFrame**_. The simplest way to visualise these two structures is to use an analogy with your favourite Spreadsheet application. Think of a `pandas` Series as Column A of Sheet 1 of your spreadsheet. Looking at the screen grab below it has 1 dimension (Column A) that represents the Series values, plus the row numbers which represent the indexes. A Dataframe is the whole spreadsheet, 2 dimensions or multiple columns, but more of that later.

This is what a Series looks like in a Spreadsheet.

![Series spreadsheet](https://bites-data.s3.us-east-2.amazonaws.com/series_spreadsheet.png)

In a spreadsheet the row indexes typically start at `1` and the column names typically start at `A`. The Series called `A` above has four value `[1, 2, 3, 4]`.

This is what a similar Series looks like in `pandas`:

```python
>>> x
0    1
1    2
2    3

Name: Fred, dtype: int64
```

The `pandas` Series Python variable is named `x`. The default index, like all other Python objects, are zero-based so the index values are [`0, 1, 2]`vand the series values are `[1, 2, 3]`. The sample `x` series shown is called `Fred` and all the series values are of type `int64`.

### Creating Series

Now that you know everything that you need to know about `pandas` Series it's time for you to start creating some series of your own. In this Bite you are asked to complete a number of functions that each create a pandas Series. How you create each series is up to you but if you do your research you'll find that Series can be created from all different type of Python Objects:

1. Create a Series with values `[1, 2, 3, 4, 5]` of type `int64`, don't worry about the index but make `Fred` the name of the Series.
2. Create a Series with values `[0.000, 0.001, ... 0.999, 1.000]` of type `float64`, don't worry about the index.
3. Create a Series with values `[1, 2, ... 25, 26]` of type `int64`, and add an index with values `[a, b, ... y, z]` so index `a = 1`, `b = 2` ... `y = 25`, `z = 26`.
4. Create a Series with values `[A, B, ... Y, Z]` of type `object`, and add an index with values `[101, 102, ... 125, 126]` so index `101 = 'A'`, `102 = 'B'` ... `125 = 'Y'`, `126 = 'Z'`.

In the the next Bite we'll look at getting the values out of the Series in a useful manner.
