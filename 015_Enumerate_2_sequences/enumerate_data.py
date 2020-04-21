"""Bite 15. Enumerate 2 sequences
"""
names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for i, (name, country) in generator():
        print(f'{i+1}. {name:<11}{country}')


def generator():
    for i, (name, country) in enumerate(zip(names, countries)):
        yield i, (name, country)
