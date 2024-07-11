from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.chappy import module_chappy
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDO_ChappyFight import GDO_ChappyFight
from gdo.chappy.GDT_Chappy import GDT_Chappy
from gdo.chappy.GDT_Element import GDT_Element


class fight(Method):

    def gdo_trigger(self) -> str:
        return 'cpf'

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_Chappy('target').default_random(),
            GDT_Element('with').initial('man').positional(),
        ]

    def get_target(self) -> GDO_Chappy:
        return self.param_value('target')

    def gdo_execute(self):
        defender = self.get_target()
        if defender is None:
            return self.err('err_chappy_no_fight_target')
        attacker = module_chappy.instance().get_chappy(self._env_user)
        fight, outcome = GDO_ChappyFight.fight(attacker, defender, self.parameter('with'))
        return fight

