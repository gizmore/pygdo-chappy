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
        pass

    def gdo_chappy_evolve(self):
        pass

    def gdo_chappy_apply(self):
        pass

    ##########
    # Helper #
    ##########
    def val_float_to_enum(self, val: float, enum: GDT_Enum):
        choices = list(enum.init_choices().values())
        choice = choices[int(val * len(choices))]
        enum.val(choice)

