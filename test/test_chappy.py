import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import module_enabled, Random
from gdo.chappy.Factory import Factory
from gdo.chappy.module_chappy import module_chappy
from gdo.core.GDO_User import GDO_User
from gdo.core.connector.Bash import Bash
from gdo.perf.method.perf import perf
from gdotest.TestUtil import reinstall_module, install_module, cli_plug, cli_gizmore


class ChappyTest(unittest.TestCase):

    def setUp(self):
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        loader.init_cli()
        return self

    def start_chappy(self, user: GDO_User, genome_number: str):
        out = cli_plug(user, '$chappy.start')
        self.assertIn('playing Chappy! Genome Number', out, 'Cannot start chappy for gizmore.')
        user.save_setting('chappy_genome', genome_number)
        out = cli_plug(user, '$cpr')
        self.assertIn('A new chappy adventure has been started', out, 'Cannot reset chappy for gizmore.')
        chappy = module_chappy.instance().get_chappy(user)
        self.assertIsNotNone(chappy, 'cannot reset a chappy for gizmore.')
        return chappy

    def test_00_re_install(self):
        reinstall_module('blackjack')
        reinstall_module('chatgpt')
        reinstall_module('chappy')
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        loader.init_cli()
        self.assertTrue(module_enabled('chappy'), 'Cannot re-install chappy.')

    def test_01_chappy_start(self):
        self.start_chappy(cli_gizmore(), '612')

    def test_02_color(self):
        chappy = self.start_chappy(cli_gizmore(), '612')
        chappy.set_val('gene_skin', '128')
        color = chappy.render_skin_color()
        self.assertEqual(color, 'Dark Turquoise', 'Color does not work')

    def test_03_chappy_stats(self):
        gizmore = cli_gizmore()
        self.start_chappy(cli_gizmore(), '612')
        out = cli_plug(gizmore, "$cps")
        print(out)
        self.assertIn('Fuego', out, 'gizmore has no fuego hair.')

    def test_04_chappy_fight_peter(self):
        server = Bash.get_server()
        peter = server.get_or_create_user('Peter')
        peter_chappy = self.start_chappy(peter, '42')
        gizmore_chappy = self.start_chappy(cli_gizmore(), '612')
        self.assertNotEquals(peter_chappy, gizmore_chappy, 'Peter and gizmore have the same chappy.')
        out = cli_plug(cli_gizmore(), "$cpf --with fire Peter")







if __name__ == '__main__':
    unittest.main()
