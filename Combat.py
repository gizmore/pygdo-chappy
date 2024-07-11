from typing_extensions import TYPE_CHECKING

import math

if TYPE_CHECKING:
    from gdo.chappy.GDO_ChappyFight import GDO_ChappyFight


from gdo.base.Util import Random
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDT_Element import GDT_Element


class FightOutcome:
    _attacker: GDO_Chappy
    _defender: GDO_Chappy
    _atk1: int
    _atk2: int
    _dice1: int
    _dice2: int
    _life: int

    def __init__(self, attacker, defender, atk1, atk2):
        self._attacker = attacker
        self._defender = defender
        self._atk1 = atk1
        self._atk2 = atk2
        self._dice1 = Random.mrand(0, atk1)
        self._dice2 = Random.mrand(0, atk2)
        self._life = self.get_lives()

    def get_lives(self) -> int:
        atk1 = math.floor(self._dice1 + 1)
        atk2 = math.floor(self._dice2 + 1)
        diff = atk1 - atk2
        if diff > 0:
            return round(math.log10(diff))
        return -1


class Combat:

    @classmethod
    def fight(cls, fight: 'GDO_ChappyFight'):
        attacker = fight.get_attacker()
        defender = fight.get_defender()
        element = fight.get_element()
        seed = fight.get_seed()
        attacker.get_computed()
        defender.get_computed()
        atk1 = 1
        atk2 = 1
        with Random(seed):
            # Base attacker (always)
            atk1 += Random.mrand(0, int(attacker.get_attr('c_atk')))
            atk1 += Random.mrand(0, int(attacker.get_attr('c_strength') * 3.0))
            atk1 += Random.mrand(0, int(attacker.get_attr('c_quickness') * 1.5))
            atk1 += Random.mrand(0, int(attacker.get_attr('c_intelligence') * 2.0))
            # Base defender (always)
            atk2 += Random.mrand(0, int(defender.get_attr('c_def')))
            atk2 += Random.mrand(0, int(defender.get_attr('c_strength') * 1.5))
            atk2 += Random.mrand(0, int(defender.get_attr('c_quickness') * 3.0))
            atk2 += Random.mrand(0, int(defender.get_attr('c_intelligence') * 2.0))
            # Elemental
            match element:
                case GDT_Element.FIRE:
                    atk1 += Random.mrand(0, int(attacker.get_attr('c_fire')))
                    atk2 += Random.mrand(0, int(defender.get_attr('c_earth')))
                case GDT_Element.EARTH:
                    atk1 += Random.mrand(0, int(attacker.get_attr('c_earth')))
                    atk2 += Random.mrand(0, int(defender.get_attr('c_water')))
                case GDT_Element.WATER:
                    atk1 += Random.mrand(0, int(attacker.get_attr('c_water')))
                    atk2 += Random.mrand(0, int(defender.get_attr('c_fire')))

        return FightOutcome(attacker, defender, atk1, atk2)
