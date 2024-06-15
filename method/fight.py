from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.chappy.GDT_Chappy import GDT_Chappy


class fight(Method):

    def gdo_trigger(self) -> str:
        return 'cpy.fight'

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_Element('with').init('man')
            GDT_Chappy('target').default_random(),
        ]

    def get_target(self) -> GDO_Chappy:
        return self.param_value('target')

    def gdo_execute(self):
        target = self.get_target()