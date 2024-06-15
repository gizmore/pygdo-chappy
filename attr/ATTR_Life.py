from gdo.chappy.ATTR import ATTR
from gdo.core.GDT_UInt import GDT_UInt


class ATTR_Life(GDT_UInt, ATTR):

    def __init__(self, name: str):
        super().__init__(name)
        self.bytes(2)
        self.max(65535)
