from gdo.base.GDO_Module import GDO_Module


class module_chappy(GDO_Module):

    def gdo_dependencies(self) -> list:
        return [
            'avatar',
        ]

    pass
