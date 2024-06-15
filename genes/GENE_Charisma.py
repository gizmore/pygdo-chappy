from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


class GENE_Charisma(GENE_FloatEnum):

    def gdo_choices(self) -> dict:
        return {
            'ugly': 'Ugly',
            'handy': 'Handy',
            'beautiful': 'Beautiful',
        }
