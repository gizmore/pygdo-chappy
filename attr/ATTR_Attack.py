from gdo.chappy.ATTR import ATTR
from gdo.core.GDT_UInt import GDT_UInt


class ATTR_Attack(GDT_UInt, ATTR):

    def __init__(self, name: str):
        super().__init__(name)
        self.min(0)
        self.max(65535)
        self.bytes(2)

