from gdo.core.GDT_Enum import GDT_Enum


class GDT_Element(GDT_Enum):
    FIRE = 'fire'
    EARTH = 'earth'
    WATER = 'water'
    WIND = 'wind'
    ICE = 'ice'
    MAN = 'man'

    def __init__(self, name):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {
            self.FIRE: 'Fire',
            self.EARTH: 'Earth',
            self.WATER: 'Water',
            self.WIND: 'Wind',
            self.ICE: 'Ice',
            self.MAN: 'Birds',
        }

