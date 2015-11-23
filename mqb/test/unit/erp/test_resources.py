import mqb.domain.erp.resources as resources

import pytest
import pdb


class A_Part:

    def setup_method(self, method):
        self.part_number = "part_key"
        self.description = "any description"

    def should_be_initialized_as_default(self):

        part = resources.Part(self.part_number)

        assert part.number == self.part_number

    def should_be_intitalized_with_description(self):
        part = resources.Part(self.part_number, self.description)

        assert part.description == self.description


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
