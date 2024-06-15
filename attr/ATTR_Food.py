from gdo.chappy.ATTR import ATTR
from gdo.core.GDT_Int import GDT_Int


class ATTR_Food(GDT_Int, ATTR):

    def __init__(self, name: str):
        super().__init__(name)
        self.bytes(1)
        self.min(-120)
        self.max(120)
