from __future__ import annotations

from gdo.chappy.genes.GENE_FloatEnum import GENE_FloatEnum
from gdo.core.GDT_Enum import GDT_Enum


class GENE_Size(GENE_FloatEnum):
    GENOME_TEXTS = {
        'tiny': 'a tiny',
        'small': 'a small',
        'medium': 'a medium',
        'large': 'a large',
        'huge': 'a huge',
    }

    def __init__(self, name: str):
        super().__init__(name)
        self.proxy(GDT_Enum(f"{name}_enum").not_null().choices({
            'tiny': 'tiny',
            'small': 'tiny',
            'medium': 'tiny',
            'large': 'tiny',
            'huge': 'tiny',
        })).initial('small')

    def gdo_genome_text(self):
        return self.GENOME_TEXTS[self._proxy.get_val()]
