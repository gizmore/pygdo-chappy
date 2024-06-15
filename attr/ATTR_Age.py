from gdo.chappy.ATTR import ATTR
from gdo.date.GDT_Duration import GDT_Duration


class ATTR_Age(GDT_Duration, ATTR):
    """
    Age in seconds.
    """

    def __init__(self, name: str):
        super().__init__(name)
