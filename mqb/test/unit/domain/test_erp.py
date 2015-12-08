import mqb.engine.domain.erp as erp
from mqb.engine.domain.base import Concept
import pytest


class A_Batch:

    def should_be_initialized_with_defaults(self):
        concept = Concept("key")
        batch = erp.Batch(concept, "tracking number")

        assert batch.concept.key == "key"
        assert batch.tracking == "tracking number"


class An_amount:

    def should_be_initialized(self):
        batch = erp.Batch(erp.Concept("conceptKey"), "trackingNumber0")
        amount = erp.Amount(batch)

        assert amount.qty == 1
        assert amount.batch == batch


class A_Part:

    def setup_method(self, method):
        self.part_number = "part_key"
        self.description = "any description"

    def should_be_initialized_as_default(self):

        part = erp.Part(self.part_number)

        assert part.number == self.part_number

    def should_be_intitalized_with_description(self):
        part = erp.Part(self.part_number, self.description)

        assert part.description == self.description


class A_Product:

    def setup_method(self, method):
        self.part_number = "part_key"
        self.part_description = "any description"
        self.tracking = "12345"
        self.qty = 20

    def should_be_initialized_with_defaults(self):
        part = erp.Part(self.part_number, self.part_description)
        batch = erp.Batch(part, self.tracking)
        product = erp.Product(batch, self.qty)

        assert product.part.number == self.part_number
        assert product.batch.tracking == self.tracking
        assert product.qty == self.qty
