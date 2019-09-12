# Bite 180. Group names by country

## Description

In this Bite you are presented with a list of surnames, names, and countries. These 3 fields are in a multiline string, separated by a comma.

Code `group_names_by_country`, looping through the list, returning a `collections.defaultdict` where the keys are countries and the values are `list`s of concatenated names and surnames. The order of the names does not matter.

Here is an example of a possible input to your function:

```markdown
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""
```

... and the output your function should return:

```python
defaultdict(,
            {'BR': ['Alphonso Harrold'],
             'CN': ['Margo Apdell', 'Ines Parrett', 'Davie Halbard'],
             'ID': ['Husain Watsham', 'Sula Wasielewski'],
             'PL': ['Kermit Braunle'],
             'RU': ['Deerdre Tomblings'],
             'SE': ['Luke Brenston'],
             'TD': ['Rudolph Jeffry']})
```
