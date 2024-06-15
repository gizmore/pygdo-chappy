from gdo.chappy.ATTR import ATTR
from gdo.core.GDT_UInt import GDT_UInt


class ATTR_Ice(GDT_UInt, ATTR):

    def __init__(self, name: str):
        super().__init__(name)
