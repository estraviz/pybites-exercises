"""
Bite 19. Write a simple property
"""


from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, promo_time):
        self.name = name
        self.promo_time = promo_time

    @property
    def expired(self):
        return True if self.promo_time < NOW else False
