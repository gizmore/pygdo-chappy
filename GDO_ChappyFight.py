from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.base.Util import Random
from gdo.chappy.Combat import FightOutcome, Combat
from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDT_Chappy import GDT_Chappy
from gdo.chappy.GDT_Element import GDT_Element
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Int import GDT_Int
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created


class GDO_ChappyFight(GDO):
    _outcome: FightOutcome

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('cf_id'),
            GDT_Chappy('cf_attacker'),
            GDT_Chappy('cf_defender'),
            GDT_Element('cf_element'),
            GDT_UInt('cf_seed').bytes(8).not_null(),
            GDT_UInt('cf_atk1').bytes(2).max(65535),
            GDT_UInt('cf_atk2').bytes(2).max(65535),
            GDT_UInt('cf_dice1').bytes(2).max(65535),
            GDT_UInt('cf_dice2').bytes(2).max(65535),
            GDT_Int('cf_lives').bytes(1).min(-127).max(128),
            GDT_Created('cf_created'),
        ]

    def get_attacker(self) -> GDO_Chappy:
        return self.gdo_value('cf_attacker')

    def get_defender(self) -> GDO_Chappy:
        return self.gdo_value('cf_defender')

    def get_element(self) -> str:
        return self.gdo_val('cf_element')

    def get_seed(self) -> int:
        return self.gdo_value('cf_seed')

    def get_lives(self) -> int:
        return self.gdo_value('cf_lives')

    def get_attack(self) -> int:
        return self.gdo_value('cf_atk1')

    def get_defense(self) -> int:
        return self.gdo_value('cf_atk2')

    def get_attack_dice(self) -> int:
        return self.gdo_value('cf_dice1')

    def get_defense_dice(self) -> int:
        return self.gdo_value('cf_dice2')

    def get_date(self) -> str:
        return self.gdo_val('cf_created')

    def get_timestamp(self) -> float:
        return self.column('cf_created').get_timestamp()

    def has_won(self) -> bool:
        return self.get_lives() > 0

    def get_outcome(self) -> FightOutcome:
        if not hasattr(self, '_outcome'):
            with Random(self.get_seed()):
                self._outcome = Combat.fight(self)
        return self._outcome

    ##########
    # Static #
    ##########
    @classmethod
    def fight(cls, attacker: GDO_Chappy, defender: GDO_Chappy, element: GDT_Element) -> tuple['GDO_ChappyFight', FightOutcome]:
        seed = Random.mrand()
        fight = cls.blank({
            'cf_attacker': attacker.get_id(),
            'cf_defender': defender.get_id(),
            'cf_element': element.get_val(),
            'cf_seed': str(seed),
        })
        outcome = fight.get_outcome()
        fight.set_vals({
            'cf_atk1': str(outcome._atk1),
            'cf_atk2': str(outcome._atk2),
            'cf_dice1': str(outcome._dice1),
            'cf_dice2': str(outcome._dice2),
            'cf_lives': str(outcome._life),
        }).insert()
        cls.apply_outcome(attacker, defender, fight, outcome)
        return fight, outcome

    @classmethod
    def apply_outcome(cls, attacker: GDO_Chappy, defender: GDO_Chappy, fight: 'GDO_ChappyFight', outcome: FightOutcome):
        attacker.increment('c_lives', outcome.get_lives()).save()

    ##########
    # Render #
    ##########
    # nfo_chappy_fight = "%s's %s attacks %s's %s with %s: %s(%s) vs. %s(%s)."
    # info_chappy_fight_won = "It wins and steals %s health."
    # info_chappy_fight_los = "It lost!"

    def render_txt(self) -> str:
        a = self.get_attacker()
        ao = a.get_owner()
        d = self.get_defender()
        do = d.get_owner()
        txt = t('info_chappy_fight', [
            ao.render_name(),
            a.render_name(),
            do.render_name(),
            d.render_name(),
            self.get_element(),
            self.get_attack_dice(),
            self.get_attack(),
            self.get_defense_dice(),
            self.get_defense(),
        ])
        if self.has_won():
            txt += " "
            txt += t('info_chappy_fight_won', [self.get_lives()])
        else:
            txt += " "
            txt += t('info_chappy_fight_los')
        return txt
