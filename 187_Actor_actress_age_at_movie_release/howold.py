"""
Bite 187. Actor/actress age at movie release
"""

from dataclasses import dataclass

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    return f'{actor.name} was {relativedelta(parse(movie.release_date), parse(actor.born)).years} years old when {movie.title} came out.'
