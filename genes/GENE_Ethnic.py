from gdo.chappy.GENE import GENE
from gdo.core.GDT_Enum import GDT_Enum


class GENE_Ethnic(GDT_Enum, GENE):

    def __init__(self, name: str):
        super().__init__(name)

