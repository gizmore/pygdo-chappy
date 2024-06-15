from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


class GENE_Strength(GENE_FloatEnum):

    def gdo_choices(self) -> dict:
        return {
            'weak': 'weak',
            'bit_weak': 'a bit weak',
            'healthy': 'healthy',
            'good_shape': 'good',
            'strong': 'strong',
            'mighty': 'mighty',
        }
