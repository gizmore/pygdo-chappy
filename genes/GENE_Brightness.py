from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


class GENE_Brightness(GENE_FloatEnum):

    def gdo_choices(self) -> dict:
        return {
            'very dark': 'dark',
            'quite dark': 'quite dark',
            'quite bright': 'quite bright',
            'very bright': 'very bright',
        }
