from __future__ import annotations

from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


class GENE_Size(GENE_FloatEnum):

    def gdo_choices(self) -> dict:
        return {
            'tiny': 'tiny',
            'small': 'small',
            'medium': 'medium',
            'big': 'big',
            'large': 'very large',
            'huge': 'huge',
        }

    def gdo_chappy_apply(self):
        chappy = self.get_chappy()
        chappy.inc_attr('c_strength', self.get_value() * 10.0)
