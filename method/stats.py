from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.base.Trans import t
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDT_Chappy import GDT_Chappy
from gdo.core.GDT_String import GDT_String


class stats(Method):

    def gdo_trigger(self) -> str:
        return 'cps'

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_Chappy('chappy').default_own(),
        ]

    def get_chappy(self) -> GDO_Chappy:
        return self.param_value('chappy')

    def gdo_execute(self):
        chappy = self.get_chappy()
        text = t('chappy_stats', [self.get_attribute_text(chappy), self.get_genome_text(chappy)])
        return GDT_String('stats').val(text)

    def get_attribute_text(self, chappy: GDO_Chappy) -> str:
        return ''

    def get_genome_text(self, chappy: GDO_Chappy) -> str:
        return ''

