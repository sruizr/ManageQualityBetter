from mqb.domain.erp.resources import (
                                      Product,
                                      Part,
                                      Concept,
                                      Material,
                                      )


IS_OK = 0
IS_SUSPECT = 1
IS_NOK = 2


# Quality resources

class Failure(Concept):

    def __init__(self, how, what, who, failure_key=None):
        key = "{}, {}, {}".format(how.key, what.key, who.key)
        Concept.__init__(self, key)
        self.elements = [how, what, who]

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

        return Failure(how, what, who)

    def add_cause(self, cause):
        self.causes.append(cause)

    def add_efect(self, efect):
        self.efects.append(efect)

    def get_full_name(self, language):

        # temporal solucion till multilanguage translation
        return self.description


class Defect(Material):

    def __init__(self, failure_description, tracking,
                 qty=1, suspect=False):

        failure = Failure.parse(failure_description)
        Material.__init__(self, failure, tracking, qty)

        self.suspect = suspect

    @property
    def failure(self):
        return self.concept


class NcMaterial(Product):

    def __init__(self, part_number, tracking,  qty=1, defects=[]):
        Product.__init__(self, part_number, tracking, qty)
        self.defects = defects

    def add_defect(self, failure, is_nc):
        pass

    def status(self):
        if self.defects:
            status = IS_SUSPECT
            for defect in self.defects:
                if status == IS_SUSPECT:
                    status = IS_NOK if (not defect.suspect) else status
        else:
            status = IS_OK
        return status

    def copy(self):
        new_item = NcMaterial(self.track, self.failures, self.qty)
        return new_item


class CustomerIssue:

    def __init__(self, customer, key, line, nc_item, sat_user, replaced=False):
        self.key = key
        self.line = line
        self.nc_item = nc_item
        self.customer = customer
        self.sat_user = sat_user
        self.replaced = replaced




