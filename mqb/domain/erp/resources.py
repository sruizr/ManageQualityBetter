from .base import Resource

import pdb

class Material(Resource):
    """It's a material resource"""
    def __init__(self, concept, tracking, qty=1):
        self.concept = concept
        self.qty = qty
        self.tracking = tracking


class Container(Resource):

    def __init__(self, name=None):
        self._resources = []


class Concept(Resource):
    "It's a concept in the system"
    def __init__(self, key, description=None):
        Resource.__init__(self)
        self.key = key
        if description:
            self.description = description


class Part(Concept):
    "Part definition "
    def __init__(self, part_number, description=None):
        Concept.__init__(self, part_number, description)

    @property
    def number(self):
        return self.key


class Product(Material):
    def __init__(self, part_number, tracking, qty=1):
        part = Part(part_number)
        Material.__init__(self, part, tracking, qty)

    @property
    def part(self):
        return self.concept


class Document(Concept):
    pass


class Picture(Document):
    pass
