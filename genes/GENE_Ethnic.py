from gdo.base.Util import Random
from gdo.chappy.GENE import GENE
from gdo.core.GDT_Enum import GDT_Enum


class GENE_Ethnic(GDT_Enum, GENE):
    _level: int


    def __init__(self, name: str):
        super().__init__(name)
        self._level = int(name[8:9])

    def gdo_choices(self) -> dict:
        return {
            'african': 'African',
            'asian': 'Asian',
            'caucasian': 'Caucasian',
            'latin': 'Latin',
        }

    def gdo_chappy_start(self):
        if self._level == 1:
            chappy = self.get_chappy()
            chappy.set_val(self.get_name(), Random.dict_key(self.init_choices()))
