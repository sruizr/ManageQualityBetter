from mqb.domain.erp.materials import (
                                      Batch,
                                      Amount,
                                      Product,
                                      )
from mqb.domain.erp.base import(
                                Concept,
                                )


class A_Batch:

    def should_be_initialized_with_defaults(self):
        concept_key = "conceptKey"
        concept = Concept(concept_key)
        batch = Batch(concept)

        assert batch.concept == concept
        assert hasattr(batch, "tracking")


class An_Amount:

    def should_be_initialized(self):
        concept_key = "k"
        concept = Concept(concept_key)
        batch = Batch(concept)

        amount = Amount(batch)

        assert amount.batch == batch
        assert amount.qty == 1
        assert amount.concept == concept


class A_Product:

    def setup_method(self, method):
        self.part_number = "part_key"
        self.description = "any description"
        self.tracking = "12345"
        self.qty = 20

    def should_be_initialized_with_defaults(self):
        product = resources.Product(self.part_number, self.tracking)

        assert product.part.number == self.part_number
        assert product.tracking == self.tracking
        assert product.qty == 1

    def should_be_initialized_with_extra_arguments(self):
        product = resources.Product(self.part_number, self.tracking,
                                    self.qty)

        assert product.part.number == self.part_number
        assert product.tracking == self.tracking
        assert product.qty == self.qty


class An_Amount:
    def should_be_initialized_with_defaults(self):
        pass

    def should_be_initialized_with_defaults(self):
        pass
