# import pdb


class DetectionPoint:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind


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
