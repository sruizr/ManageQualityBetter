from .base import Node, Organization


class Role(Node):
    """Decorator of node"""
    def __init__(self, decorated):
        key = decorated.key + "@" + self.__class__.__name__
        Node.__init__(self, key)
        self.decorated = decorated

    def transfer(self):
        pass

    def move_work_item(self):
        pass


class Customer(Role):

    def __init__(self, key, contact_person,
                 category, language="es"):
        Role.__init__(self, contact_person)

        self.key = key
        self.category = category
        self.language = language

    @property
    def contact(self):
        return self.decorated


