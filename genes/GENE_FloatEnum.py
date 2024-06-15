from gdo.chappy.GENE import GENE
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.GDT_Float import GDT_Float
from gdo.core.WithProxy import WithProxy


class GENE_FloatEnum(WithProxy, GDT_Float, GENE):
    """
    FloatEnum maps a float from 0-1 to an enum with fair distribution.
    Order enums from bad to good
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.proxy(GDT_Enum(f"{name}_enum").choices(self.gdo_choices()))

    def val(self, val: str | list):
        self.val_float_to_enum(float(val), self._proxy)
        return super().val(val)

    def gdo_choices(self) -> dict:
        return {}
