
class Customer:

    def __init__(self, name, mail_address, type, language):
        self.name = name
        self.mail_address = mail_address
        self.type = type
        self.language = language


class User:

    def __init__(self, id, name, full_name, mail_address):
        self._id = id
        self.name = name
        self.full_name = full_name
        self.mail_address = mail_address


class Document:

    def __init__(self, name):
        self.path = None
        self.name = name


class CustomerIssue:

    def __init__(self, id, line_number):
        self.id = id
        self.line_number = line_number


class FailureStatement:

    def __init__(self, part, tracking, failure, qty=1):
        self.part = part
        self.tracking = tracking
        self.failure = failure
        self.qty = qty


class Failure:

    def __init__(self, id, where, what, how):
        self.id = id
        self.where = where
        self.what = what
        self.how = how
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
