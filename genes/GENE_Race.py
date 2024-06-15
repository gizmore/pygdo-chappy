from gdo.chappy.GENE import GENE
from gdo.core.GDT_Decimal import GDT_Decimal


class GENE_Race(GDT_Decimal, GENE):

    RACES = [

    ]

    def __init__(self, name: str):
        super().__init__(name)


