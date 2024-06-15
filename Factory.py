from gdo.chappy.GDO_Chappy import GDO_Chappy
from gdo.chappy.GDT_ChappyGenome import GDT_ChappyGenome
from gdo.chatgpt.module_chatgpt import module_chatgpt
from gdo.core.GDO_User import GDO_User


class Factory:

    @classmethod
    def new_chappy(cls, user: GDO_User, active: bool = False) -> GDO_Chappy:
        if active:
            if old_chappy := GDO_Chappy.active_for_user(user):
                old_chappy.deactivate()
        device = module_chatgpt.instance().cfg_chappy(user=user)
        data = {
            'c_name': device.get_displayname(),
            'c_owner': user.get_id(),
            'c_device': device.get_id(),
            'c_active': '1' if active else '0',
        }
        chappy = GDO_Chappy.blank(data)
        for key in chappy.GENES:
            chappy.column(key).gdo_chappy_start()
        chappy.insert().make_active()
        return chappy
