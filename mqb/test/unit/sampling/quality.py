from .erp import get_product
from mqb.engine.domain.quality import (
                                       Failure,
                                       NcMaterial,
                                       Defect,
                                       Issue,
                                       )
from mqb.engine.domain.base import Node
from random import randrange
import pdb

def get_nc_product(index, defects_qty, detection):

    product = get_product(index)
    nc_material = NcMaterial(product.batch, randrange(1, defects_qty))
    for defect_index in range(1, defects_qty):
        add_defect(defect_index, nc_material, detection)

    return nc_material


def add_defect(index, nc_material, detection):
    tracking = detection.key + str(index)
    defect = Defect(nc_material, detection, get_failure(index), tracking)


def get_failure(index):
    failure_description = "incorrect{1} attribute{1} on element{1}".format(index)
    failure = Failure.parse(failure_description)
    return failure


def get_issue(index, nc_qty):
    detection = Node("detectionKey" + str(index))
    issue_key = "issue" + str(index)
    issue = Issue(issue_key, detection)

    for line in range(0, nc_qty+1):
        nc_material = get_nc_product(line, randrange(nc_qty), detection)
        issue.nc_materilas[str(line)] = nc_material

    return issue
