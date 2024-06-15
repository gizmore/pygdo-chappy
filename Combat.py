from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDT_Element import GDT_Element


class Outcome:
    _attacker: GDO_Chappy
    _defender: GDO_Chappy
    _atk1: int
    _atk2: int
    _life: int

    def __init__(self, attacker, defender, atk1, atk2, life):
        self._attacker = attacker
        self._defender = defender
        self._atk1 = atk1
        self._atk2 = atk2
        self._life = life

class Combat:

    @classmethod
    def fight(cls, attacker: GDO_Chappy, defender: GDO_Chappy, element: GDT_Element):

        pass