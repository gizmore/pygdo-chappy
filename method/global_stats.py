from gdo.base.Method import Method
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDO_ChappyFight import GDO_ChappyFight


class global_stats(Method):

    def gdo_trigger(self) -> str:
        return 'cpgs'

    def gdo_execute(self):
        fights = GDO_ChappyFight.table()
        chaps = GDO_Chappy.table()
        total = chaps.count_where()
        active = chaps.count_where('c_active')
        idle = total - active
        return self.msg('msg_chappy_global_stats', [
            fights.count_where(),
            total,
            active,
            idle,
        ])
