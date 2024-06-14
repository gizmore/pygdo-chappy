from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.chappy.attr.ATTR_Strength import ATTR_Strength
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_User import GDT_User


class GDO_Chappy(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('c_id'),
            GDT_User('c_user'),
            GDT_User('c_device'),
            ATTR_Strength('c_str'),

        ]
