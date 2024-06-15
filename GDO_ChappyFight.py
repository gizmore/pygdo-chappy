from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Util import Random
from gdo.chappy.Combat import FightOutcome, Combat
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDT_Chappy import GDT_Chappy
from gdo.chappy.GDT_Element import GDT_Element
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created


class GDO_ChappyFight(GDO):
    _outcome: FightOutcome

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('cf_id'),
            GDT_Chappy('cf_attacker'),
            GDT_Chappy('cf_defender'),
            GDT_Element('cf_element'),
            GDT_UInt('cf_seed').not_null(),
            GDT_UInt('cf_atk1').bytes(2).max(65535),
            GDT_UInt('cf_atk2').bytes(2).max(65535),
            GDT_Created('cf_created'),
        ]

    def get_attacker(self) -> GDO_Chappy:
        return self.gdo_value('cf_attacker')

    def get_defender(self) -> GDO_Chappy:
        return self.gdo_value('cf_defender')

    def get_element(self) -> str:
        return self.gdo_val('cf_element')

    def get_seed(self) -> int:
        return self.gdo_value('cf_seed')

    def get_attack(self) -> int:
        return self.gdo_value('cf_atk1')

    def get_defense(self) -> int:
        return self.gdo_value('cf_atk2')

    def get_date(self) -> str:
        return self.gdo_val('cf_created')

    def get_timestamp(self) -> float:
        return self.column('cf_created').get_timestamp()

    def get_outcome(self) -> FightOutcome:
        if not hasattr(self, '_outcome'):
            with Random(self.get_seed()):
                self._outcome = Combat.fight(self)
        return self._outcome

    ##########
    # Static #
    ##########
    @classmethod
    def fight(cls, attacker: GDO_Chappy, defender: GDO_Chappy, element: GDT_Element) -> tuple['GDO_ChappyFight', FightOutcome]:
        seed = Random.mrand()
        fight = cls.blank({
            'cf_attacker': attacker.get_id(),
            'cf_defender': defender.get_id(),
            'cf_element': element.get_val(),
            'cf_seed': str(seed),
        })
        outcome = fight.get_outcome()
        return fight, outcome
