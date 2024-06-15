from gdo.base.Logger import Logger
from gdo.chappy.WithChappy import WithChappy
from gdo.core.GDT_Field import GDT_Field


class ATTR(WithChappy, GDT_Field):

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_apply_attribute(self):
        Logger.error("STUB")
        