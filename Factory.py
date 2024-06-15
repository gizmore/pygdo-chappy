from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDT_ChappyGenome import GDT_ChappyGenome
from gdo.chatgpt.module_chatgpt import module_chatgpt
from gdo.core.GDO_User import GDO_User


class Factory:

    @classmethod
    def new_chappy(cls, user: GDO_User, active: bool = False) -> GDO_Chappy:
        device = module_chatgpt.instance().cfg_chappy(user=user)
        data = {
            'c_name': device.get_name(),
            'c_owner': user.get_id(),
            'c_device': device.get_id(),
            'c_active': '1' if active else '0',
        }
        chappy = GDO_Chappy.blank(data)
        genome = GDT_ChappyGenome()
        genome.gdo()

        chappy.insert().make_active()
        return chappy
