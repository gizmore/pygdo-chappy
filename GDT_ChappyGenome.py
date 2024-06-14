from gdo.base.GDT import GDT
from gdo.chappy.genes.GENE_HairLength import GENE_HairLength
from gdo.core.GDT_Composite import GDT_Composite


class GDT_ChappyGenome(GDT_Composite):

    def gdo_components(self) -> list[GDT]:
        return [
            GENE_HairLength(),
        ]
