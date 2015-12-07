from mqb.engine.domain.erp import (
                               Product,
                               Batch,
                               Amount,
                               Part,
                               )
from mqb.engine.domain.base import Node
from random import randrange


def get_product(index):
    tracking = "productionTracking" + str(index)
    batch = Batch(get_part(index), tracking)

    qty = randrange(1, index)
    return Product(batch, qty)


def get_part(index):
    part_number = "partNumber" + str(index)
    return Part(part_number, "This is a description of " + part_number)


def get_customer(index):
    return Node("customerKey")
