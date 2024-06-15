from gdo.base.Logger import Logger
from gdo.chappy.WithChappy import WithChappy
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.GDT_Field import GDT_Field


class GENE(WithChappy, GDT_Field):

    def __init__(self, name):
        super().__init__(name)

    ############
    # Abstract #
    ############
    def gdo_chappy_start(self):
        Logger.error("STUB")

    def gdo_chappy_evolve(self):
        Logger.error("STUB")

    def gdo_chappy_apply(self):
        Logger.error("STUB")

    ##########
    # Helper #
    ##########
    def val_float_to_enum(self, val: float, enum: GDT_Enum):
        choices = enum.init_choices()
        choice = choices[int(val * len(choices))]
        enum.val(choice)

