from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDT_Chappy import GDT_Chappy
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User


class module_chappy(GDO_Module):

    def gdo_classes(self):
        return [
            GDO_Chappy,
        ]

    def gdo_dependencies(self) -> list:
        return [
            'account',
            'avatar',
            'blackjack',
            'chatgpt',
        ]

    def gdo_user_config(self) -> list[GDT]:
        return [
            GDT_UInt('chappy_genome'),
            GDT_Chappy('chappy'),  # The chappy instance to play with.
        ]

    def get_chappy(self, user: GDO_User) -> GDO_Chappy:
        return user.get_setting_value('chappy')

