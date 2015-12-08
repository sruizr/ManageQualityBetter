from .erp import get_product
from mqb.engine.domain.quality import (
                                       Failure,
                                       NcMaterial,
                                       Defect,
                                       Issue,
                                       )
from mqb.engine.domain.base import Node
import pdb


def get_nc_product(index, defects_qty, detection):

    product = get_product(index)
    nc_material = NcMaterial(product.batch, defects_qty)
    for defect_index in range(1, defects_qty):
        add_defect(defect_index, nc_material, detection)

    return nc_material


def add_defect(index, nc_material, detection):
    tracking = detection.key + str(index)
    defect = Defect(nc_material, detection, get_failure(index), tracking)


def get_failure(index):
    failure_description = "incorrect{0} attribute{0} on element{0}".format(index)
    failure = Failure.parse(failure_description)
    return failure


def get_issue(index, nc_qty):
    detection = Node("detectionKey" + str(index))
    issue_key = "issue" + str(index)
    issue = Issue(issue_key, detection)

    for line in range(1, nc_qty+1):
        nc_material = get_nc_product(line, line, detection)
        issue.nc_materials[str(line)] = nc_material

    return issue
