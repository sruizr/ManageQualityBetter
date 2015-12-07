class NoInputsFound(Exception):
    pass


class IncorrectNodeClass(Exception):
    pass


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
