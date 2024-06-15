import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import module_enabled
from gdo.chatgpt import module_chatgpt
from gdo.core.GDO_User import GDO_User
from gdotest.TestUtil import reinstall_module, install_module


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

    def test_01_chappy_start(self):
        plug_cli('')
        id = module_chatgpt.instance().cfg_chappy().get_id()
        self.assertIsNotNone(id, 'Cannot get chappy id.')
        user = module_chatgpt.instance().cfg_chappy()
        self.assertIsInstance(user, GDO_User, 'Cannot get chappy user.')
        self.assertEqual(id, user.get_id(), 'ID User mismatch for cfg_chappy().')


if __name__ == '__main__':
    unittest.main()
