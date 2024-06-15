from gdo.chappy.ATTR import ATTR
from gdo.core.GDT_UInt import GDT_UInt


class ATTR_Level(GDT_UInt, ATTR):

    def __init__(self, name: str):
        super().__init__(name)
        self.max(10000)
        self.bytes(2)
