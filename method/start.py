from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.base.Util import Random


class start(Method):

    def gdo_trigger(self) -> str:
        return 'cpy.start'

    def gdo_parameters(self) -> [GDT]:
        return []

    def gdo_execute(self):
        user = self._env_user
        genome_number = user.get_setting_val('chappy_genome')
        if genome_number:
            return self.err('err_chappy_already_started', [genome_number])
        genome_number = Random.mrand(0, 1123456789)
        self._env_user.save_setting('chappy_genome', str(genome_number))
        return self.msg('msg_chappy_started', [genome_number])
