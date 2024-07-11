from gdo.chappy.ATTR import ATTR
from gdo.date.GDT_Timestamp import GDT_Timestamp
from gdo.date.Time import Time


class ATTR_Age(GDT_Timestamp, ATTR):
    """
    Age in seconds.
    """

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_before_create(self, gdo):
        gdo.set_val(self._name, Time.get_date())
