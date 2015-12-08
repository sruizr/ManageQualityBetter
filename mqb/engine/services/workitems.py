from mqb.domain.base import WorkItem, Container


class Product(WorkItem):

    def __init__(self, part, qty=1, tracking=None):
        self.part = part
        self.qty = qty
        if tracking:
            self.tracking = tracking


class NcMaterial(Container):

    def __init__(self, product, defects):
        self.product = product
        self.defects = defects

    def is_defective(self):
        pass


class Defect(WorkItem):

    def __init__(self, failure, confirmed=True, qty=1, tracking=None):
        WorkItem.__init__(self, failure, qty, tracking)
        self.confirmed = confirmed
