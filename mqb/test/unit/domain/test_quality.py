from mqb.engine.domain.quality import (
                                       Failure,
                                       NcMaterial,
                                       Defect,
                                       Issue,
                                       Function,
                                       IS_OK,
                                       IS_SUSPECT,
                                       IS_NOK
                                       )
from mqb.engine.domain.base import Concept, Node
from mqb.engine.domain.erp import Part, Batch
import pdb
from ..sampling import quality as q


class A_Failure:

    def should_init_with_defaults(self):
        how = Concept("incorrect")
        what = Concept("attribute")
        who = Concept("element")

        function = Function(what, who)
        failure = Failure(how, function)

        assert failure.function == function
        assert failure.how == how
        assert hasattr(failure, "causes")
        assert hasattr(failure, "efects")

    def could_initialized_with_description(self):
        failure_description = "incorrect attribute at element"
        failure = Failure.parse(failure_description)

        assert failure.function.key == "attribute, element"
        assert failure.how.key == "incorrect"
        assert failure.key == "incorrect, attribute, element"

    def should_give_a_description(self):
        failure_description = "incorrect attribute at element"
        failure = Failure.parse(failure_description)

        assert failure.get_description() == "incorrect attribute @ element"


class A_Defect:

    def should_be_initialized(self):
        pass


class A_NcMaterial:
    def setup_method(self, method):
        self.part = Part("partnumber")
        self.batch = Batch(self.part, "trackingNumber")
        self.qty = 10

        self.nc_material = NcMaterial(self.batch, self.qty)

    def teardown_method(self, method):
        self.nc_material.defects = None
        self.nc_material = None

    def add_defect(self, index):
        detection_point = Node("nodeKey")
        tracking = "detectionTracking" + str(index)
        qty = 2
        suspect = False
        failure = Failure.parse("incorrect{0} feature{0} at element{0}".format(
                                str(index)))
        defect = Defect(self.nc_material,
                        detection_point, failure, tracking,
                        qty,
                        suspect)
        return defect

    def should_be_initialized(self):

        assert self.nc_material.qty == self.qty
        assert self.nc_material.batch == self.batch

    def should_receive_defects(self):

        defect = self.add_defect(0)
        assert self.nc_material.defects[0] == defect
        assert defect.qty == 2
        assert defect.detection_point.key == "nodeKey"

    def should_has_a_status(self):

        # Status IS_OK
        assert self.nc_material.status() == IS_OK

        # Status IS_NOK
        self.add_defect(1)
        self.add_defect(2)
        assert self.nc_material.status() == IS_NOK

        # Status IS_SUSPECT
        self.nc_material.defects[0].suspect = True
        self.nc_material.defects[1].suspect = True
        assert self.nc_material.status() == IS_SUSPECT


class An_Issue:

    def should_be_initialized(self):

        key = "INC0001"
        detection = Node("nodeKey")
        issue = Issue(key, detection)

        assert issue.detection == detection
        assert issue.key == key
