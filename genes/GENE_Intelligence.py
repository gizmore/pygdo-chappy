from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


class GENE_Intelligence(GENE_FloatEnum):

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {
            'dumb': 'a bit dumb',
            'clueless': 'a bit clueless',
            'puzzled': 'a bit puzzled',
            'witty': 'witty',
            'smart': 'smart',
            'genius': 'like a genius'
        }
