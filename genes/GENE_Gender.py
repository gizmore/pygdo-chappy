from gdo.base.Util import Random
from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


class GENE_Gender(GENE_FloatEnum):

    def __init__(self, name):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {
            'male': 'Male',
            'female': 'Female',
        }

    def gdo_chappy_start(self):
        self.get_chappy().set_val(self.get_name(), Random.mrandf(0, 1.0))
