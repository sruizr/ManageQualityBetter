from .base import Material


class Batch(Material):

    def __init__(self, concept, tracking=None):
        Material.__init__(self, concept)
        self.tracking = tracking


class Amount(Batch):

    def __init__(self, batch, qty=1):
        self.batch = batch
        self.qty = qty


class Product(Amount):
    def __init__(self, part_number, tracking, qty=1):

        part = Part(part_number)
        Material.__init__(self, part, tracking, qty)

    @property
    def part(self):
        return self.concept
