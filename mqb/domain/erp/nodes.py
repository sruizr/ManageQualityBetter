from .base import Node


class Role(Node):
    """Decorator of node"""
    def __init__(self, decorated):
        self.decorated = decorated

    def transfer(self):
        pass

    def move_work_item(self):
        pass


class Person(Node):
    def __init__(self, name):
        Node.__init__(self)
        self.name = name
        self.mail_address = None
        self.full_name = None
        self.roles = []


class Machine(Node):
    def __init__(self, name):
        Node.__init__(self)
        self.name = name


class Organization(Node):

    def __init__(self, name=None):
        self.name = name
        self.nodes = []


class Customers(Organization):

    def __init__(self, customers=None):
        Organization.__init__(self, name="customers")
        if customers:
            self.customers = customers


class Customer(Organization):

    def __init__(self, name, mail_address, category, language="es"):
        self.name = name
        self.mail_address = mail_address
        self.category = category
        self.language = language


