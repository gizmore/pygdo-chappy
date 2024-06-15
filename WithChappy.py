from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.core.GDO_User import GDO_User
from gdo.core.WithGDO import WithGDO


class WithChappy(WithGDO):

    def get_chappy(self) -> GDO_Chappy:
        """
        Get the GDO_Chappy in-game avatar.
        """
        return self._gdo

    def get_user_user(self) -> GDO_User:
        return self.get_chappy().get_owner()

    def get_chappy_user(self) -> GDO_User:
        return self.get_chappy().get_chappy_user()

