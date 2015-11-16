from mqb.domain.base import Resource

class Document(Resource):
    pass


class Picture(Document):
    pass


class Part(Resource):

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Failure(Resource):

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

        # temporal solucion till multilanguage translation
        return self.description
