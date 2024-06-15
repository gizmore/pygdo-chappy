from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


class GENE_Quickness(GENE_FloatEnum):

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {
            'slow': 'slow',
            'lazy': 'a bit lazy',
            'fast': 'fast',
            'very_fast': 'very fast',
            'incredible_fast': 'incredibly fast',
        }
