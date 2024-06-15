from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


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

    def get_race_strength(self) -> int:
        return round(self.get_value() * self.NUM_RACES)

    def get_race_quickness(self) -> int:
        match self._proxy.get_val():
            case 'hummingbird':
                return 10
            case 'sparrow':
                return 9
            case 'robin':
                return 8
            case 'toucan':
                return 4
            case 'kingfisher':
                return 5
            case 'blue_jay':
                return 7
            case 'woodpecker':
                return 7
            case 'penguin':
                return 2
            case 'parrot':
                return 4
            case 'crow':
                return 6
            case 'flamingo':
                return 2
            case 'owl':
                return 4
            case 'dove':
                return 5
            case 'seagull':
                return 5
            case 'pelican':
                return 2
            case 'swan':
                return 2
            case 'eagle':
                return 4
            case 'hawk':
                return 5
            case 'heron':
                return 3
            case 'peacock':
                return 3
            case _:
                return 0

    def gdo_apply_genome(self):
        chappy = self.get_chappy()
        chappy.inc_attr('c_strength', self.get_race_strength())
        chappy.inc_attr('c_quickness', self.get_race_quickness())


