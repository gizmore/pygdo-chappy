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
        # chappy_stats_0 = "%s belongs to %s, is %s %s %s %s." # Name User a small caucasian male race.
        stats_txt = t('chappy_stats_0', [
            chappy.get_chappy_name(),
            chappy.get_owner().get_displayname(),
            chappy.column('gene_size').gdo_chappy_genome_text(),
        ])
        #self.get_attribute_text(chappy), self.get_genome_text(chappy)
        text = t('chappy_stats', [stats_txt])
        return GDT_String('stats').val(text)

    def get_attribute_text(self, chappy: GDO_Chappy) -> str:
        return ''

    def get_genome_text(self, chappy: GDO_Chappy) -> str:
        return ''

