from gdo.core.GDT_Enum import GDT_Enum


class GDT_Element(GDT_Enum):

    def __init__(self, name):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {
            'fire': 'Fire',
            'earth': 'Earth',
            'water': 'Water',
            'wind': 'Wind',
            'ice': 'Ice',
            'man': 'Man',
        }

