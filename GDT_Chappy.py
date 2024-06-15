from __future__ import annotations

from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_ObjectSelect import GDT_ObjectSelect


class GDT_Chappy(GDT_ObjectSelect):
    """
    Get a chappy.
    """
    _own: bool
    # _dead: bool
    _random: bool

    def __init__(self, name):
        super().__init__(name)
        self._own = False
        # self._dead = False
        self._random = False
        self.table(GDO_Chappy.table())

    ###########
    # Options #
    ###########
    # def dead(self, dead: bool = True):
    #     self._dead = dead
    #     return self

    def default_own(self, own: bool = True):
        self._own = own
        return self

    def default_random(self, random: bool = True):
        self._random = random
        return self

    def get_value(self):
        value = super().get_value()
        if value is None:
            user = GDO_User.current()
            if self._own:
                return GDO_Chappy.active_for_user(user)
            if self._random:
                return GDO_Chappy.random_except_for_user(user)
        return value
