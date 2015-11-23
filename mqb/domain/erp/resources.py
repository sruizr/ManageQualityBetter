class Material(Resource):
    """It's a material resource"""
    def __init__(self, concept, qty=1):
        self.concept = concept
        self.qty = qty


class Container(Resources):

    def __init__(self, name=None):
        self._resources = []


class Concept(Resource):
    "It's a concept in the system"
    def __init__(self, category=None):
        if category:
            self.category = category
