from __future__ import annotations

from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum


class GENE_WingSize(GENE_FloatEnum):

    def gdo_choices(self) -> dict:
        return {
            'tiny': 'tiny',
            'small': 'small',
            'medium': 'medium',
            'big': 'big',
            'large': 'very large',
            'huge': 'huge',
        }
