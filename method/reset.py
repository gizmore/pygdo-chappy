from gdo.base.Method import Method
from gdo.chappy.Factory import Factory


class reset(Method):

    def gdo_trigger(self) -> str:
        return 'cpr'

    def gdo_execute(self):
        user = self._env_user
        genome_number = user.get_setting_val('chappy_genome')
        if not genome_number:
            return self.err('err_chappy_game_not_started')
        chappy = Factory.new_chappy(user, active=True)
        return self.msg('msg_chappy_reset', [genome_number])
