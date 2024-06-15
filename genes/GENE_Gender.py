from gdo.chappy.GENE import GENE
from gdo.user.GDT_Gender import GDT_Gender


class GENE_Gender(GDT_Gender, GENE):

    def __init__(self, name):
        super().__init__(name)
