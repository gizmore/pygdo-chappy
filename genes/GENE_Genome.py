from gdo.chappy.GENE import GENE
from gdo.core.GDT_String import GDT_String


class GENE_Genome(GDT_String, GENE):

    def __init__(self, name):
        super().__init__(name)
