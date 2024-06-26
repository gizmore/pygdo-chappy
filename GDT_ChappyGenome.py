from __future__ import annotations

from gdo.base.GDT import GDT
from gdo.chappy.genes.GENE_Brightness import GENE_Brightness
from gdo.chappy.genes.GENE_Charisma import GENE_Charisma
from gdo.chappy.genes.GENE_Ethnic import GENE_Ethnic
from gdo.chappy.genes.GENE_EyeColor import GENE_EyeColor
from gdo.chappy.genes.GENE_FeatherColor import GENE_FeatherColor
from gdo.chappy.genes.GENE_Gender import GENE_Gender
from gdo.chappy.genes.GENE_HairColor import GENE_HairColor
from gdo.chappy.genes.GENE_HairLength import GENE_HairLength
from gdo.chappy.genes.GENE_Intelligence import GENE_Intelligence
from gdo.chappy.genes.GENE_Quickness import GENE_Quickness
from gdo.chappy.genes.GENE_Race import GENE_Race
from gdo.chappy.genes.GENE_Size import GENE_Size
from gdo.chappy.genes.GENE_Strength import GENE_Strength
from gdo.chappy.genes.GENE_WingSize import GENE_WingSize
from gdo.core.GDT_Composite import GDT_Composite
from gdo.core.WithGDO import WithGDO


class GDT_ChappyGenome(WithGDO, GDT_Composite):
    """
    All chappy genes in one composite.
    """

    def gdo_components(self) -> list[GDT]:
        return [
            GENE_Gender('gene_gender').not_null(),
            GENE_Race('gene_race').not_null(),
            GENE_Ethnic('gene_eth1').not_null(),
            GENE_Ethnic('gene_eth2'),
            GENE_Ethnic('gene_eth3'),
            GENE_Size('gene_size').not_null(),
            GENE_WingSize('gene_wing_size').not_null(),
            GENE_Strength('gene_str').not_null(),
            GENE_Quickness('gene_qui').not_null(),
            GENE_Intelligence('gene_int').not_null(),
            GENE_Charisma('gene_cha').not_null(),
            GENE_FeatherColor('gene_feather_color').not_null(),
            GENE_HairColor('gene_hair').not_null(),
            GENE_EyeColor('gene_eyes').not_null(),
            GENE_Brightness('gene_skin').not_null(),
            GENE_HairLength('gene_hair_len').not_null(),
        ]

    #########
    # Reset #
    #########
    def initialize_reset_chappy(self):
        for gdt in self.gdo_components():
            gdt.gdo(self._gdo)
            gdt.gdo_
        pass
