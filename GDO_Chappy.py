from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.chappy.attr.ATTR_Age import ATTR_Age
from gdo.chappy.attr.ATTR_Attack import ATTR_Attack
from gdo.chappy.attr.ATTR_Defense import ATTR_Defense
from gdo.chappy.attr.ATTR_Earth import ATTR_Earth
from gdo.chappy.attr.ATTR_Fire import ATTR_Fire
from gdo.chappy.attr.ATTR_Food import ATTR_Food
from gdo.chappy.attr.ATTR_Ice import ATTR_Ice
from gdo.chappy.attr.ATTR_Joy import ATTR_Joy
from gdo.chappy.attr.ATTR_Life import ATTR_Life
from gdo.chappy.attr.ATTR_Quickness import ATTR_Quickness
from gdo.chappy.attr.ATTR_Strength import ATTR_Strength
from gdo.chappy.attr.ATTR_Water import ATTR_Water
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_User import GDT_User
from gdo.core.GDT_UserName import GDT_UserName


class GDO_Chappy(GDO):

    def gdo_columns(self) -> list[GDT]:
        from gdo.chappy.GDT_ChappyGenome import GDT_ChappyGenome
        return [
            GDT_AutoInc('c_id'),
            GDT_UserName('c_name'),
            GDT_User('c_owner').not_null().cascade_delete(),
            GDT_User('c_device').cascade_delete(),
            GDT_Bool('c_active').not_null().initial('0'),
            # real
            ATTR_Age('c_age'),
            ATTR_Life('c_lives'),
            ATTR_Food('c_food'),
            ATTR_Joy('c_joy'),
            # computed
            ATTR_Strength('c_strength'),
            ATTR_Quickness('c_quickness'),
            ATTR_Strength('c_intelligence'),
            ATTR_Quickness('c_charisma'),
            ATTR_Attack('c_atk'),  # for all elements
            ATTR_Defense('c_def'),  # for all elements
            ATTR_Fire('c_fire'),  # against earth
            ATTR_Earth('c_earth'),  # against water
            ATTR_Water('c_water'),  # against fire
            ATTR_Ice('c_ice'),
            # genome
            GDT_ChappyGenome(),

        ]

    def get_owner(self) -> GDO_User:
        return self.gdo_value('c_owner')

    def get_chappy_user(self) -> GDO_User:
        return self.gdo_value('c_device')

    def make_active(self):
        return self
