from mqb.domain.resources import (
                                  NcMaterial,
                                  Defect,
                                  Failure,
                                  IS_OK,
                                  IS_SUSPECT,
                                  IS_NOK,
                                  )
from mqb.domain.erp.resources import Concept


import pytest


class A_Failure:
    def setup_method(self, method):
        self.who = Concept("product")
        self.what = Concept("performance")
        self.how = Concept("low")
        self.description = "low performance at product"

    def should_be_initialized_with_defaults(self):
        failure = Failure(self.how, self.what, self.who)

        assert failure.key == "{}, {}, {}".format(self.how.key, self.what.key,
                                                  self.who.key)
        assert failure.elements

    def should_parse_failure_from_a_description(self):

        failure = Failure.parse(self.description)

        assert failure.elements[0].key == self.how.key
        assert failure.elements[1].key == self.what.key
        assert failure.elements[2].key == self.who.key


class A_Defect:

    def setup_method(self, method):
        self.failure_description = "low performance at product"
        self.failure_key = "low, performance, product"
        self.qty = 20
        self.suspect = True
        self.tracking = "12345"

    def should_be_initialized_with_defaults(self):
        defect = Defect(self.failure_description, self.tracking)

        assert defect.failure.key == self.failure_key
        assert not defect.suspect
        assert defect.qty == 1
        assert defect.tracking == self.tracking

    def should_be_initialized_with_optional_parameters(self):
        defect = Defect(self.failure_description, self.tracking, self.qty,
                        self.suspect)

        assert defect.suspect == self.suspect
        assert defect.qty == self.qty
        assert defect.failure.key == self.failure_key
        assert defect.tracking == self.tracking


class A_NcMaterial:

    def setup_method(self, method):
        self.part_number = "partNumber"
        self.description = "Part description"
        self.tracking = "12345"
        self.qty = 20
        self.issue_number = "INC1234-01"

        self.nok_defect = Defect("low performance at product", self.issue_number)
        self.suspect_defect = Defect("incorrect performance at product component",
                               self.issue_number, 1, True)

    def should_be_initialized_with_defaults(self):
        nc_material = NcMaterial(self.part_number, self.tracking)

        assert nc_material.part.number == self.part_number
        assert nc_material.tracking == self.tracking
        assert nc_material.qty == 1
        assert not nc_material.defects

    def should_be_initialized_with_extra_arguments(self):
        nc_material = NcMaterial(self.part_number, self.tracking, self.qty,
                                 [self.nok_defect, self.suspect_defect])

        assert nc_material.part.number == self.part_number
        assert nc_material.tracking == self.tracking
        assert nc_material.qty == self.qty
        assert len(nc_material.defects) == 2

    def should_know_material_status(self):

        nc_ok = NcMaterial(self.part_number, self.tracking)

        assert nc_ok.status() == IS_OK

        nc_nok = NcMaterial(self.part_number, self.tracking, 1,
                            [self.nok_defect])

        assert nc_nok.status() == IS_NOK

        nc_suspect = NcMaterial(self.part_number, self.tracking, 1,
                                [self.suspect_defect])

        assert nc_suspect.status() == IS_SUSPECT
