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
        owner = chappy.get_owner()
        # chappy_stats_0a = "%s belongs to %s, and is a %s level %s %s."  # Name User a level 11 small male cat.
        # chappy_stats_0b = "%s belongs to %s, is s %s %s mixture of %s(%s%%) and %s(%s%%)%s. It has level %s."  # Name User a small caucasian male race.

        if not chappy.is_mixture():
            txt1 = t('chappy_stats_0a', [
                chappy.get_chappy_name(),
                owner.get_displayname(),
                chappy.render_size(),
                chappy.get_level(),
                chappy.render_gender(),
                chappy.render_race1(),
            ])
        else:
            txt1 = t('chappy_stats_0b', [
                chappy.get_chappy_name(),
                owner.get_displayname(),
                chappy.render_size(),
                chappy.render_gender(),
                chappy.render_race1(),
                chappy.render_race1_percent(),
                chappy.render_race2(),
                chappy.render_race2_percent(),
                chappy.get_level(),
            ])

        # chappy_stats_1 = "It is %s old, has %s skin, %s hair, which %s cm long, and %s eyes." # 5y brown, blue, 13cm blonde eyes
        txt2 = t('chappy_stats_1', [
            chappy.render_age(),
            chappy.render_skin_color(),
            chappy.render_hair_color(),
            chappy.render_hair_length(),
            chappy.render_eye_color(),
        ])

        txt3 = t('chappy_stats_2', [
            chappy.render_quickness(),
            chappy.render_strength(),
            chappy.render_charisma(),
            chappy.render_intelligence(),
        ])

        text = f"{txt1} {txt2} {txt3}"

        # txt4 = t('chappy_stats_3', [
        #     self.render_attributes(chappy),
        # ])
        #
        #
        # # chappy_stats_1 = "It is %s old, has %s %scm long headhair, %s eyes and %s %s wings." # 5y 13cm haircolor, eyecolor, little wingcolor
        # stats_txt = t('chappy_stats_0', [
        #     chappy.get_chappy_name(),
        #     owner.get_displayname(),
        #     chappy.column('gene_size').gdo_chappy_genome_text(),
        # ])
        # #self.get_attribute_text(chappy), self.get_genome_text(chappy)
        # text = t('chappy_stats', [stats_txt])
        return GDT_String('stats').val(text)

    # def render_attributes(self, chappy: GDO_Chappy) -> str:
    #     text = []
    #     keys = {
    #         'gene_str': 'STR',
    #         'gene_int': 'INT',
    #         'gene_qui': 'QUI',
    #         'gene_cha': 'CHA',
    #     }
    #     for key, lbl in keys.values():
    #         val = chappy.gdo_value(key) * 100
    #         text.append(f"{lbl}: {}")
    #         text.append(f"STR: {chappy.gdo_value('gene_str'):1f}")
    #     return ', '.join(text)

    def get_genome_text(self, chappy: GDO_Chappy) -> str:
        return ''

