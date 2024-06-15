from gdo.base.Util import Random
from gdo.chappy.GENE import GENE
from gdo.core.GDT_Float import GDT_Float


class GENE_HairLength(GDT_Float, GENE):
    """
    The birds top hair length in cm
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.min(0.0)
        self.max(20.0)

    def gdo_chappy_start(self):
        chappy = self.get_chappy()
        chappy.set_val(self.get_name(), Random.mrandf(0, 10.0))
