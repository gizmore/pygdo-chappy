from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.chappy.GDT_ChappyGenome import GDT_ChappyGenome
from gdo.chappy.attr.ATTR_Attack import ATTR_Attack
from gdo.chappy.attr.ATTR_Strength import ATTR_Strength
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_User import GDT_User


class GDO_Chappy(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('c_id'),
            GDT_User('c_owner'),
            GDT_User('c_device'),  # chappy user
            GDT_Bool('c_active'),
            # real
            ATTR_Strength('c_str'),
            # computed
            ATTR_Attack('c_atk'),
            # genome
            GDT_ChappyGenome(),

        ]

    def get_owner(self) -> GDO_User:
        return self.gdo_value('c_owner')

    def get_chappy_user(self) -> GDO_User:
        return self.gdo_value('c_device')
