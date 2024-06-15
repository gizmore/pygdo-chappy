from __future__ import annotations

from gdo.base.GDT import GDT
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.genes.GENE_Brightness import GENE_Brightness
from gdo.chappy.genes.GENE_Ethnic import GENE_Ethnic
from gdo.chappy.genes.GENE_EyeColor import GENE_EyeColor
from gdo.chappy.genes.GENE_HairColor import GENE_HairColor
from gdo.chappy.genes.GENE_HairLength import GENE_HairLength
from gdo.chappy.genes.GENE_Intelligence import GENE_Intelligence
from gdo.chappy.genes.GENE_Quickness import GENE_Quickness
from gdo.chappy.genes.GENE_Race import GENE_Race
from gdo.chappy.genes.GENE_Strength import GENE_Strength
from gdo.core.GDT_Composite import GDT_Composite


class GDT_ChappyGenome(GDT_Composite):

    def gdo_components(self) -> list[GDT]:
        return [
            GENE_Race('gene_race'),
            GENE_Ethnic('gene_eth1'),
            GENE_Ethnic('gene_eth2'),
            GENE_Ethnic('gene_eth3'),
            GENE_Strength('gene_str'),
            GENE_Quickness('gene_qui'),
            GENE_Intelligence('gene_int'),
            GENE_HairColor('gene_hair'),
            GENE_Brightness('gene_skin'),
            GENE_HairLength('gene_hair_len'),
            GENE_EyeColor('gene_eyes'),
        ]
    @classmethod
    def genome_text(cls, chappy: GDO_Chappy):
        text = t('chappy_genome_text_template', [
            self.
        ])

    @classmethod
    def create(cls, genome_number: int):
        Random.with_seed(genome_number):
            
        pass

    def gdo_components(self) -> list[GDT]:
        pass


