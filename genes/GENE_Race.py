from gdo.chappy.GENE import GENE
from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum
from gdo.core.GDT_Decimal import GDT_Decimal


class GENE_Race(GENE_FloatEnum):
    NUM_RACES = 20

    def gdo_choices(self) -> dict:
        return {
            'hummingbird': 'Hummingbird',
            'sparrow': 'Sparrow',
            'robin': 'Robin',
            'toucan': 'Toucan',
            'kingfisher': 'Kingfisher',
            'blue_jay': 'Blue Jay',
            'woodpecker': 'Woodpecker',
            'penguin': 'Penguin',
            'parrot': 'Parrot',
            'crow': 'Crow',
            'flamingo': 'Flamingo',
            'owl': 'Owl',
            'dove': 'Dove',
            'seagull': 'Seagull',
            'pelican': 'Pelican',
            'swan': 'Swan',
            'eagle': 'Eagle',
            'hawk': 'Hawk',
            'heron': 'Heron',
            'peacock': 'Peacock',
        }

    def __init__(self, name: str):
        super().__init__(name)

    def get_base_strength(self) -> int:
        return round(self.get_value() * self.NUM_RACES)

    def get_base_quickness(self) -> int:
        match self._proxy.get_val():
            case _:
                return 10

    def gdo_apply_genome(self):
        chappy = self.get_chappy()


