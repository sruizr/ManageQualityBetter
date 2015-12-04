from .base import (
                   Resource,
                   Concept,
                   Material,
                   Information,
                   )

import pdb


class Batch(Material):

    def __init__(self, concept, tracking):
        Material.__init__(self, concept)
        self.tracking = tracking


class Amount(Material):

    def __init__(self, batch, qty=1):
        Material.__init__(self, batch.concept)
        self.batch = batch
        self.qty = qty


class Part(Concept):
    "Part definition "
    def __init__(self, part_number, description=None):
        Concept.__init__(self, part_number, description)

    @property
    def number(self):
        return self.key


class Product(Amount):
    def __init__(self, batch, qty=1):
        Amount.__init__(self, batch, qty)

    @property
    def part(self):
        return self.concept



class Document(Concept):
    pass


class Picture(Document):
    pass
