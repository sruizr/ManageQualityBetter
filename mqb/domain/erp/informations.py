from .base import Resource


class Information(Resource):

    def __init__(self, concept, template=None):
        Resource.__init__(self)
        self.concept = concept
        self.template = template


class Document(Information):
    pass
