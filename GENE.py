from gdo.base.Logger import Logger
from gdo.chappy.WithChappy import WithChappy
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.GDT_Field import GDT_Field


class GENE(WithChappy, GDT_Field):

    def __init__(self, name):
        super().__init__(name)

    def gdo_apply_genome(self):
        Logger.error("STUB")

    def gdo_genome_text(self) -> str:
        return f"With {self.get_name()}\n"

    def val_float_to_enum(self, val: float, enum: GDT_Enum):
        choices = enum.init_choices()
        choice = choices[int(val * len(choices))]
        enum.val(choice)

    def gdo_evolve(self):
        pass