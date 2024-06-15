import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import module_enabled, Random
from gdo.chappy import module_chappy
from gdo.chatgpt import module_chatgpt
from gdo.core.GDO_User import GDO_User
from gdotest.TestUtil import reinstall_module, install_module, cli_plug, cli_gizmore


class ChappyTest(unittest.TestCase):

    def setUp(self):
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        install_module('chappy')
        install_module('chatgpt')
        install_module('blackjack')
        loader.init_modules(True, True)
        loader.init_cli()
        return self

    def test_00_re_install(self):
        reinstall_module('chappy')
        reinstall_module('chatgpt')
        reinstall_module('blackjack')
        self.assertTrue(module_enabled('chappy'), 'Cannot re-install chappy.')

    def test_01_random(self):
        with Random(42):
            a1 = Random.mrand(1, 100)
            b1 = Random.mrand(1, 100)
        self.assertGreater(a1, 0, 'Random.mrand not working.')
        with Random(42):
            a2 = Random.mrand(1, 100)
            b2 = Random.mrand(1, 100)
        self.assertEqual(a1, a2, 'Random.mrand not working a1==a2')
        self.assertEqual(b1, b2, 'Random.mrand not working b1==b2')

    def test_02_chappy_start(self):
        cli_plug(None, '$cpy.start')
        cli_plug(None, '$cpr')
        chappy = module_chappy.instance().get_chappy(cli_gizmore())
        self.assertIsNotNone(chappy, 'cannot reset a chappy.')


if __name__ == '__main__':
    unittest.main()
