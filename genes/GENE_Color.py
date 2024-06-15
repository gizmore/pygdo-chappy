from gdo.chappy.GENE import GENE
from gdo.core.GDT_UInt import GDT_UInt


class GeneColor(GDT_UInt, GENE):
    """
    Hair Color of your chappy. Uses HSV for smooth genetics.
    Greenish hair gives most attack.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.min(0)
        self.max(255)
        self.bytes(1)

    def get_rgb(self):

    def gdo_apply_gene(self):
