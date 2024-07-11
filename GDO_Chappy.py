import colorsys

from gdo.base.Application import Application
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
from gdo.chappy.genes.GENE_Brightness import GENE_Brightness
from gdo.chappy.genes.GENE_Charisma import GENE_Charisma
from gdo.chappy.genes.GENE_EyeColor import GENE_EyeColor
from gdo.chappy.genes.GENE_Gender import GENE_Gender
from gdo.chappy.genes.GENE_HairColor import GENE_HairColor
from gdo.chappy.genes.GENE_HairLength import GENE_HairLength
from gdo.chappy.genes.GENE_Intelligence import GENE_Intelligence
from gdo.chappy.genes.GENE_Quickness import GENE_Quickness
from gdo.chappy.genes.GENE_Race import GENE_Race
from gdo.chappy.genes.GENE_Size import GENE_Size
from gdo.chappy.genes.GENE_SkinColor import GENE_SkinColor
from gdo.chappy.genes.GENE_Strength import GENE_Strength
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_User import GDT_User
from gdo.core.GDT_UserName import GDT_UserName
from gdo.date.Time import Time


class GDO_Chappy(GDO):
    _computed: dict[str, int]

    GENES = [
        'gene_gender',
        'gene_race1_enum',
        'gene_race2_enum',
        # 'gene_eth1',
        # 'gene_eth2',
        # 'gene_eth3',
        'gene_size',
        # 'gene_wing_size',
        'gene_str',
        'gene_qui',
        'gene_int',
        'gene_cha',
        'gene_skin',
        'gene_hair',
        'gene_eyes',
        'gene_brightness',
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
        return [
            GDT_AutoInc('c_id'),
            GDT_UserName('c_name'),
            GDT_User('c_owner').not_null().cascade_delete(),
            GDT_User('c_device').cascade_delete(),
            GDT_Bool('c_active').not_null().initial('0'),
            GDT_Bool('c_dead').not_null().initial('0'),
            # real
            ATTR_Level('c_level').not_null().initial('1'),
            ATTR_Age('c_birthdate'),
            ATTR_Life('c_lives').initial('100').min(0).max(100),
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
            GENE_Gender('gene_gender').not_null(),
            GENE_Race('gene_race1').not_null(),
            GENE_Race('gene_race2').not_null(),
            # GENE_Ethnic('gene_eth1').not_null(),
            # GENE_Ethnic('gene_eth2'),
            # GENE_Ethnic('gene_eth3'),
            GENE_Size('gene_size').not_null(),
            # GENE_WingSize('gene_wing_size').not_null(),
            GENE_Strength('gene_str').not_null(),
            GENE_Quickness('gene_qui').not_null(),
            GENE_Intelligence('gene_int').not_null(),
            GENE_Charisma('gene_cha').not_null(),
            GENE_SkinColor('gene_skin').not_null(),
            GENE_HairColor('gene_hair').not_null(),
            GENE_EyeColor('gene_eyes').not_null(),
            GENE_Brightness('gene_brightness').not_null(),
            GENE_HairLength('gene_hair_len').not_null(),
        ]

    def get_chappy_name(self):
        return self.gdo_val('c_name')

    def get_owner(self) -> GDO_User:
        return self.gdo_value('c_owner')

    def get_chappy_user(self) -> GDO_User:
        return self.gdo_value('c_device')

    def make_active(self):
        self.get_owner().save_setting('chappy', self.get_id())
        return self

    def deactivate(self):
        self.save_val('c_active', '0')
        self.delete()
        return self

    def is_male(self) -> bool:
        return self.get_gender() == 'male'

    def is_female(self) -> bool:
        return self.get_gender() == 'female'

    def get_gender(self) -> str:
        return self.column('gene_gender').enum_val()

    def get_level(self) -> int:
        return self.gdo_value('c_level')

    def get_birthdate(self) -> float:
        return self.gdo_value('c_birthdate')

    def get_age(self) -> float:
        duration = Application.TIME - Time.get_time(self.get_birthdate())
        duration *= 52
        return Time.get_age_in_years(duration)

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

    def get_attr(self, key: str) -> any:
        return self._computed[key]

    def is_mixture(self) -> bool:
        return self.gdo_val('gene_race2_enum') is not None

    ##########
    # Render #
    ##########
    def render_gender(self) -> str:
        return self.column('gene_gender').render_txt()

    def render_size(self) -> str:
        return self.column('gene_size').enum_proxy().render_txt()

    def render_race1(self):
        return self.column('gene_race1_enum').render_race()

    def render_race2(self):
        return self.column('gene_race2_enum').render_race()

    def render_race1_percent(self):
        return self.column('gene_race1_percent').render_txt()

    def render_race2_percent(self):
        return self.column('gene_race2_percent').render_txt()

    def render_age(self) -> str:
        return str(Time.get_age_in_years(self.get_age()))

    def render_hair_length(self) -> str:
        return str(self.gdo_value('gene_hair_len'))

    def render_hair_color(self) -> str:
        return self.render_color(self.gdo_value('gene_hair'))

    def render_skin_color(self) -> str:
        return self.render_color(self.gdo_value('gene_skin'))

    def render_eye_color(self) -> str:
        return self.render_color(self.gdo_value('gene_eyes'))

    def get_rgb(self, hue: int) -> str:
        h = hue / 255.0
        l = self.gdo_value('gene_brightness')
        s = 1.0
        rf, gf, bf = colorsys.hls_to_rgb(h, l, s)
        rf = int(rf * 255.0)
        gf = int(gf * 255.0)
        bf = int(bf * 255.0)
        return f"#{rf:02x}{gf:02x}{bf:02x}"

    def render_color(self, hue: int) -> str:
        rgb = self.get_rgb(hue)
        from ntc import NTC
        return NTC().name(rgb, 'en')['color']['name']

    def render_quickness(self):
        return self.column('gene_qui').render_txt()

    def render_strength(self):
        return self.column('gene_str').render_txt()

    def render_charisma(self):
        return self.column('gene_cha').render_txt()

    def render_intelligence(self):
        return self.column('gene_int').render_txt()


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

