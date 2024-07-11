from gdo.base.GDT import GDT
from gdo.base.Util import Random
from gdo.base.WithName import WithName
from gdo.chappy.GENE import GENE
from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum
from gdo.chappy.genes.GENE_RaceEnum import GENE_RaceEnum
from gdo.core.GDT_Composite import GDT_Composite
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.GDT_UInt import GDT_UInt


class GENE_Race(WithName, GDT_Composite, GENE):
    NUM_RACES = 20
    _race: GENE_RaceEnum
    _percent: GDT_UInt

    def __init__(self, name: str):
        super().__init__(name)
        self.name(name)
        self._race = GENE_RaceEnum(f"{name}_enum")
        self._percent = GDT_UInt(f"{name}_percent").min(0).max(100).bytes(1)

    def gdo_components(self) -> list['GDT']:
        return [
            self._race,
            self._percent,
        ]

    def get_level(self) -> int:
        name = self.get_name()
        return int(name[9:])

    def gdo_apply_genome(self):
        pass
        # chappy = self.get_chappy()
        # chappy.inc_attr('c_strength', self.get_race_strength())
        # chappy.inc_attr('c_quickness', self.get_race_quickness())


