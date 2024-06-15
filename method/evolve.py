from gdo.base.Method import Method


class evolve(Method):

    def gdo_trigger(self) -> str:
        return 'cpe'
