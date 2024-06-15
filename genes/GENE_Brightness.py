from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


class GENE_Brightness(GENE_FloatEnum):

    def gdo_choices(self) -> dict:
        return {
            'dark': 'dark',
            'bright': 'bright',
        }
