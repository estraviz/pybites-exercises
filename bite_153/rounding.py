from math import floor, ceil


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    return [ceil(item) if up else floor(item) for item in transactions]
