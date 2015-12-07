from mqb.engine.domain.erp import (
                                      Product,
                                      Part,
                                      Concept,
                                      Material,
                                      Batch,
                                      Amount
                                      )
from mqb.engine.domain.base import Container
import pdb

IS_OK = 0
IS_SUSPECT = 1
IS_NOK = 2


class NcMaterial(Product):

    def __init__(self, batch,  qty=1, defects=None):
        Product.__init__(self, batch, qty)
        self.defects = defects

    def status(self):
        if self.defects:
            status = IS_SUSPECT
            for defect in self.defects:
                if status == IS_SUSPECT:
                    status = IS_NOK if (not defect.suspect) else status
        else:
            status = IS_OK
        return status


class Issue(Container):

    def __init__(self, key, detection):
        Container.__init__(self, key)
        self.detection = detection

    @property
    def nc_materials(self):
        return self.resources

    @nc_materials.setter
    def nc_materials(self, value):
        self.resources = value


class Function(Concept):

    def __init__(self, what, who):
        key = "{}, {}".format(what.key, who.key)

        Concept.__init__(self, key)
        self.what = what
        self.who = who


class Failure(Concept):

    def __init__(self, failure_mode, function):
        key = "{}, {}".format(failure_mode.key, function.key)

        Concept.__init__(self, key)
        self.how = failure_mode
        self.function = function
        self.causes = []
        self.efects = []

    def get_description(self, lang=None):
        if lang is None:
            result = "{} {} @ {}".format(self.how.key,
                                         self.function.what.key,
                                         self.function.who.key)
        return result

    @classmethod
    def parse(cls, description):
        """Structure of failure description is:
        * 'failure mode'- one word
        * 'function/feature'- one word
        * (optional) link of length 2
        * 'who has failured'- Rest of words """
        elements = description.split(" ")
        how = elements[0]
        what = elements[1]
        i = 3
        if len(elements[2]) > 2:
            i = 2
        who = " ".join(elements[i:])

        how = Concept(how)
        what = Concept(what)
        who = Concept(who)

        function = Function(what, who)

        return Failure(how, function)

    def add_cause(self, cause):
        self.causes.append(cause)

    def add_efect(self, efect):
        self.efects.append(efect)


class Defect(Amount):

    def __init__(self, nc_material, detection_point, failure, tracking,
                 qty=1, suspect=False):
        self.nc_material = nc_material
        self.detection_point = detection_point
        if nc_material.defects is None:
            nc_material.defects = []
        nc_material.defects.append(self)
        batch = Batch(failure, tracking)
        Amount.__init__(self, batch, qty)
        self.suspect = suspect

    @property
    def failure(self):
        return self.concept
