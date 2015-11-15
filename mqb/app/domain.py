# import pdb

class DetectionPoint:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind


class Customer(DetectionPoint):

    def __init__(self, name, mail_address, kind, language):
        DetectionPoint.__init__(self, name, kind)
        self.mail_address = mail_address
        self.language = language


class User:

    def __init__(self, name, full_name, mail_address):
        self.name = name
        self.full_name = full_name
        self.mail_address = mail_address


class Document:

    def __init__(self, name):
        self.path = None
        self.name = name


class Picture(Document):
    pass


class Track:

    def __init__(self, part, tracking):
        self.part = part
        self.tracking = tracking


class CustomerIssue:

    def __init__(self, customer, key, line, nc_item, sat_user, replaced=False):
        self.key = key
        self.line = line
        self.nc_item = nc_item
        self.customer = customer
        self.sat_user = sat_user
        self.replaced = replaced


class NcItem:

    def __init__(self, track, failureStates, qty=1):
        self.track = track
        self.failureStates = list(failureStates)
        self.qty = qty

    def copy(self):
        new_item = NcItem(self.track,
                          self.failures, self.qty)
        return new_item


class LogisticInspection:

    def __init__(self, responsible):
        self.responsible = responsible


class Qactivity:

    def __init__(self, responsible):
        self.responsible = responsible
        self.inputs = set()

    def add_input(self, nc_item):
        self.inputs.add(nc_item)

    def process_input(self, nc_item, failureState, qty=None):
        if nc_item not in self.inputs:
            self.add_input(nc_iterm)
        if qty is None:
            qty = nc_item.qty

        result = NcItem(nc_item.track, failureState, qty)
        nc_item.origin = result
        nc_item.source = self

    def close_input(self, nc_item, failureState):
        pass

    def lost_input(self, nc_iterm, failureState):
        pass


class Inspection(Qactivity):
    pass


class Detection(Qactivity):
    pass


class Failure:

    def __init__(self, description=None):
        self.description = description
        self.causes = []
        self.efects = []
        self.S = 0
        self.O = 0

    def add_cause(self, cause):
        self.causes.append(cause)

    def add_efect(self, efect):
        self.efects.append(efect)

    def get_full_name(self, language):

        where_name = self.where.get_name(language)
        what_name = self.what.get_name(language)
        how_name = self.how.get_name(language)

        if language == "es":
            full_name = "%1 %2 de %3".format(how_name, what_name, where_name)
        elif language == "en":
            full_name = "%1 %2 at %3".format(how_name, what_name, where_name)
        else:
            raise LanguageException(language)
        return full_name


class Concept:

    def __init__(self, id, type):
        self.id = id
        self.name = {}

    def add_name(self, name, language):
        self.name[language] = name

    def get_name(self, language):
        if self.name[language]:
            name = self.name[language]
        else:
            raise LanguageException(language, self)
        return name


class LanguageException(Exception):

    def __init__(self, language, instance):
        self.language = language
        self.instance = instance

    def __str__(self):
        return "No translation for language %1 at %2 . id: %3".format(
                                      self.language,
                                      self.instance.__class__.__name__,
                                      self.instance.id
                                      )
