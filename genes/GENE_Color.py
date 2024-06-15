import colorsys

from gdo.base.Util import Random
from gdo.chappy.GENE import GENE
from gdo.core.GDT_UInt import GDT_UInt


class GENE_Color(GDT_UInt, GENE):
    """
    Color your chappy. Uses HLS for smooth genetics.
    Uses RGB to enhance stats.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.min(0)
        self.max(255)
        self.bytes(1)

    def get_rgb(self) -> tuple:
        rf, gf, bf = colorsys.hls_to_rgb(self.get_value() / 255, 0.5, 0.75)
        return round(rf * 255), round(gf * 255), round(bf * 255)

    def gdo_chappy_start(self):
        chappy = self.get_chappy()
        chappy.set_val(self.get_name(), Random.mrand(0, 255))

    def gdo_chappy_apply(self):
        chappy = self.get_chappy()
        r, g, b = self.get_rgb()
        chappy.inc_attr('c_fire', r)
        chappy.inc_attr('c_earth', g)
        chappy.inc_attr('c_water', b)
