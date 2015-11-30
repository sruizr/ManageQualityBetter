from .base import Resource


class Concept(Resource):

    def __init__(self, key):
        Resource.__init__(self, key)
        self.description = None


class Part(Concept):
    "Part definition "
    def __init__(self, part_number, description=None):
        Concept.__init__(self, part_number, description)

    @property
    def number(self):
        return self.key
