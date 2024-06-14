from gdo.base.Logger import Logger
from gdo.core.GDT_Field import GDT_Field
from gdo.core.WithGDO import WithGDO


class GENE(WithGDO, GDT_Field):

    def __init__(self, name):
        super().__init__(name)

    def gdo_apply_gene(self):
        Logger.error("STUB")
