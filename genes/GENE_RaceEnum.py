import functools

import tomlkit

from gdo.base.Util import Random
from gdo.chappy.GENE import GENE
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.GDT_UInt import GDT_UInt


class GENE_RaceEnum(GDT_Enum, GENE):

    @classmethod
    @functools.cache
    def load_data(cls) -> dict:
        from gdo.chappy.module_chappy import module_chappy
        mod = module_chappy.instance()
        path = mod.file_path('res/races.toml')
        with open(path) as fp:
            return tomlkit.load(fp)

    def gdo_choices(self) -> dict:
        data = self.load_data()
        dict = {}
        for i in data:
            dict[i] = i
        return dict

    def get_level(self) -> int:
        return int(self.get_name()[9:10])

    def get_percent_name(self) -> str:
        return self.get_name()[0:10] + "_percent"

    def get_percent_gdt(self) -> GDT_UInt:
        return self.get_chappy().column(self.get_percent_name())

    def gdo_chappy_start(self):
        if self.get_level() == 1:
            races = GENE_RaceEnum.load_data()
            val = Random.dict_key(races)
            chappy = self.get_chappy()
            chappy.set_val(self.get_name(), val)
            chappy.set_val(self.get_percent_name(), '100')

    def gdo_chappy_apply(self):
        self.apply_gene_attribute(0, 'c_strength', 'gene_str')
        self.apply_gene_attribute(1, 'c_quickness', 'gene_qui')
        self.apply_gene_attribute(2, 'c_intelligence', 'gene_int')
        self.apply_gene_attribute(3, 'c_charisma', 'gene_cha')

    def apply_gene_attribute(self, index: int, attr_key: str, gene_key: str):
        race = self.get_val()
        if race is not None:
            races = GENE_RaceEnum.load_data()
            chappy = self.get_chappy()
            factor = chappy.gdo_value(gene_key)
            max = races[race]['attributes'][index]
            ist = factor * max
            chappy.inc_attr(attr_key, round(ist))

    def gene_attribute(self, index: int, key: str):
        races = GENE_RaceEnum.load_data()
        pass

    ##########
    # Render #
    ##########
    def render_race(self) -> str:
        return self.render_txt()

