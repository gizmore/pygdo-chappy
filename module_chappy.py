from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User


class module_chappy(GDO_Module):

    def gdo_dependencies(self) -> list:
        return [
            'avatar',
            'chatgpt',
        ]

    def gdo_user_config(self) -> list[GDT]:
        return [
            GDT_UInt('chappy_genome'),
            GDT_User('chappy_user'),  # The chappy instance to play with.
        ]

