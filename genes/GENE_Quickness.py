from gdo.chappy.GENE import GENE
from gdo.core.GDT_Float import GDT_Float


class GENE_Quickness(GDT_Float, GENE):

    def __init__(self, name: str):
        super().__init__(name)
