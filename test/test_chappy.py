import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import module_enabled, Random
from gdo.chappy.module_chappy import module_chappy
from gdotest.TestUtil import reinstall_module, install_module, cli_plug, cli_gizmore


class ChappyTest(unittest.TestCase):

    def setUp(self):
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        loader.init_cli()
        return self

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
        out = cli_plug(None, '$chappy.start')
        self.assertIn('You are now playing Chappy!', out, 'Cannot start chappy.')
        print(out)
        out = cli_plug(None, '$cpr')
        print(out)
        chappy = module_chappy.instance().get_chappy(cli_gizmore())
        self.assertIsNotNone(chappy, 'cannot reset a chappy.')


if __name__ == '__main__':
    unittest.main()
