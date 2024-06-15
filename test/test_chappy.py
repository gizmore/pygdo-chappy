import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import module_enabled, Random
from gdo.chappy.module_chappy import module_chappy
from gdo.core.GDO_User import GDO_User
from gdo.core.connector.Bash import Bash
from gdotest.TestUtil import reinstall_module, install_module, cli_plug, cli_gizmore


class ChappyTest(unittest.TestCase):

    def setUp(self):
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        loader.init_cli()
        return self

    def start_chappy(self, user: GDO_User):
        out = cli_plug(user, '$chappy.start')
        self.assertIn('playing Chappy! Genome Number', out, 'Cannot start chappy for gizmore.')
        out = cli_plug(user, '$cpr')
        self.assertIn('A new chappy adventure has been started', out, 'Cannot reset chappy for gizmore.')
        chappy = module_chappy.instance().get_chappy(cli_gizmore())
        self.assertIsNotNone(chappy, 'cannot reset a chappy for gizmore.')

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
        self.start_chappy(cli_gizmore())

    def test_03_chappy_fight_peter(self):
        self.test_01_chappy_start()
        server = Bash.get_server()
        peter = server.get_or_create_user('Peter')
        self.start_chappy(peter)


if __name__ == '__main__':
    unittest.main()
