from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.chappy.attr.ATTR_Age import ATTR_Age
from gdo.chappy.attr.ATTR_Attack import ATTR_Attack
from gdo.chappy.attr.ATTR_Charisma import ATTR_Charisma
from gdo.chappy.attr.ATTR_Defense import ATTR_Defense
from gdo.chappy.attr.ATTR_Earth import ATTR_Earth
from gdo.chappy.attr.ATTR_Fire import ATTR_Fire
from gdo.chappy.attr.ATTR_Food import ATTR_Food
from gdo.chappy.attr.ATTR_Ice import ATTR_Ice
from gdo.chappy.attr.ATTR_Intelligence import ATTR_Intelligence
from gdo.chappy.attr.ATTR_Joy import ATTR_Joy
from gdo.chappy.attr.ATTR_Level import ATTR_Level
from gdo.chappy.attr.ATTR_Life import ATTR_Life
from gdo.chappy.attr.ATTR_Mankind import ATTR_Mankind
from gdo.chappy.attr.ATTR_Quickness import ATTR_Quickness
from gdo.chappy.attr.ATTR_Strength import ATTR_Strength
from gdo.chappy.attr.ATTR_Water import ATTR_Water
from gdo.chappy.attr.ATTR_Wind import ATTR_Wind
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_User import GDT_User
from gdo.core.GDT_UserName import GDT_UserName


class GDO_Chappy(GDO):
    _computed: dict[str, int]

    GENES = [
        'gene_gender',
        'gene_race',
        'gene_eth1',
        'gene_eth2',
        'gene_eth3',
        'gene_size',
        'gene_wing_size',
        'gene_str',
        'gene_qui',
        'gene_int',
        'gene_cha',
        'gene_feather_color',
        'gene_hair',
        'gene_eyes',
        'gene_skin',
        'gene_hair_len',
    ]

    COMPUTED_ATTRS = [
        'c_strength',
        'c_quickness',
        'c_intelligence',
        'c_charisma',
        'c_atk',
        'c_def',
        'c_fire',
        'c_earth',
        'c_water',
        'c_ice',
        'c_wind',
        'c_mankind',
    ]

    def __init__(self):
        super().__init__()
        self._computed = {}

    def gdo_columns(self) -> list[GDT]:
        from gdo.chappy.GDT_ChappyGenome import GDT_ChappyGenome
        return [
            GDT_AutoInc('c_id'),
            GDT_UserName('c_name'),
            GDT_User('c_owner').not_null().cascade_delete(),
            GDT_User('c_device').cascade_delete(),
            GDT_Bool('c_active').not_null().initial('0'),
            # real
            ATTR_Level('c_level'),
            ATTR_Age('c_age'),
            ATTR_Life('c_lives'),
            ATTR_Food('c_food'),
            ATTR_Joy('c_joy'),
            # computed
            ATTR_Strength('c_strength'),
            ATTR_Quickness('c_quickness'),
            ATTR_Intelligence('c_intelligence'),
            ATTR_Charisma('c_charisma'),
            ATTR_Attack('c_atk'),
            ATTR_Defense('c_def'),
            ATTR_Fire('c_fire'),
            ATTR_Earth('c_earth'),
            ATTR_Water('c_water'),
            ATTR_Ice('c_ice'),
            ATTR_Wind('c_wind'),
            ATTR_Mankind('c_mankind'),
            # genome
            GDT_ChappyGenome(),
        ]

    def get_owner(self) -> GDO_User:
        return self.gdo_value('c_owner')

    def get_chappy_user(self) -> GDO_User:
        return self.gdo_value('c_device')

    def make_active(self):
        self.get_owner().save_setting('chappy', self.get_id())
        return self

    def deactivate(self):
        self.save_val('c_active', '0')
        return self

    def is_male(self) -> bool:
        return self.get_gender() == 'male'

    def is_female(self) -> bool:
        return self.get_gender() == 'female'

    def get_gender(self) -> str:
        return self.column('gene_gender').enum_val()

    ############
    # Computed #
    ############
    def get_computed(self) -> dict[str, int]:
        if not self._computed:
            # Base value to computed
            for key in self.COMPUTED_ATTRS:
                self._computed[key] = self.gdo_value(key)
            # Add genes
            for key in self.GENES:
                self.column(key).gdo_chappy_apply()
        return self._computed

    def inc_attr(self, key: str, by: int) -> 'GDO_Chappy':
        self._computed[key] += by
        return self

    ##########
    # Static #
    ##########
    @classmethod
    def active_for_user(cls, user: GDO_User) -> 'GDO_Chappy':
        return cls.table().get_by_vals({
            'c_owner': user.get_id(),
            'c_active': '1',
        })

    @classmethod
    def all_for_user(cls, user: GDO_User) -> list['GDO_Chappy']:
        return cls.table().select().where(f"c_owner={user.get_id()}").exec().fetch_all()

    @classmethod
    def random_except_for_user(cls, user: GDO_User) -> 'GDO_Chappy':
        return cls.table().select().where(f"c_owner!={user.get_id()} AND c_active").limit(1).exec().fetch_object()
