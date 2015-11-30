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
