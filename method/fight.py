from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDT_Chappy import GDT_Chappy
from gdo.chappy.GDT_Element import GDT_Element


class fight(Method):

    def gdo_trigger(self) -> str:
        return 'cpf'

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_Element('with').init('man'),
            GDT_Chappy('target').default_random(),
        ]

    def get_target(self) -> GDO_Chappy:
        return self.param_value('target')

    def gdo_execute(self):
        target = self.get_target()
