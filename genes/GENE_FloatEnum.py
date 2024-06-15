from gdo.base.Util import Random
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
        self.proxy(GDT_Enum(f"{name}").choices(self.gdo_choices()))

    def val(self, val: str | list):
        if not val:
            val = 0
        self.val_float_to_enum(float(val), self._proxy)
        return super().val(val)

    def enum_val(self) -> str:
        return self._proxy.get_val()

    def gdo_choices(self) -> dict:
        return {}

    def gdo_column_define(self) -> str:
        return GDT_Float.gdo_column_define(self)

    def enum_proxy(self) -> GDT_Enum:
        return self._proxy

    ###########
    # Compute #
    ###########
    def gdo_chappy_start(self):
        self.get_chappy().set_val(self.get_name(), Random.mrandf(0, 0.5))

    def gdo_chappy_genome_text(self):
        return self.enum_proxy().get_value()



