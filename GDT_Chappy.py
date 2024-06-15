from __future__ import annotations

from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.core.GDT_ObjectSelect import GDT_ObjectSelect


class GDT_Chappy(GDT_ObjectSelect):
    _random: bool

    def default_random(self, random: bool = True):
        self._random = random
        return self

    def __init__(self, name):
        super().__init__(name)
        self._random = False
        self.table(GDO_Chappy.table())
