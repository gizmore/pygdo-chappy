from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.chappy import module_chappy
from gdo.chappy.Combat import FightOutcome
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDO_ChappyFight import GDO_ChappyFight
from gdo.chappy.GDT_Chappy import GDT_Chappy
from gdo.chappy.GDT_Element import GDT_Element
from gdo.core.GDO_Server import GDO_Server


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
        self.broadcast_fight(fight, outcome)
        return fight

    def broadcast_fight(self, fight: GDO_ChappyFight, outcome: FightOutcome):
        output = fight.render_txt()
        self.broadcast(fight)

    def broadcast(self, gdt: GDT):
        for server in GDO_Server.table().all():
            self.broadcast_server(server, gdt)

    def broadcast_server(self, server: GDO_Server, gdt: GDT):
        mode = server.get_connector().get_render_mode()
        msg = gdt.render(mode)
        for channel in server._channels:
            if self.is_enabled():
                channel.send(msg)

    def is_enabled(self):
        return not self.get_config_channel('disabled')
