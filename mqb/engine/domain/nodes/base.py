from ..base import Node, Movement, Resource


class Role(Node):
    """Decorator of node"""
    def __init__(self, key, decorated):
        Node.__init__(self, key)
        self.decorated = decorated

    def transfer(self):
        pass

    def move_work_item(self):
        pass


class Organization(Node):
    """It's a group of nodes, a team when all are persons"""
    def __init__(self, key, nodes={}):
        Node.__init__(self, key)

        self.nodes = nodes
        for node in self.nodes.values():
            node._parent = self

    def add_node(self, node, role_name):
        self.nodes[role_name] = node
        node._parent = self

    def remove_node(self, role_name):
        node = self.nodes.pop(role_name)
        node._parent = None


class Person(Node):
    def __init__(self, key, mail_address=None, firstname=None,
                 surname=None, genre=None, language="es"):
        Node.__init__(self, key)
        self.mail_address = mail_address
        self.firstname = firstname
        self.surname = surname
        self.genre = genre
        self.language = language

    def full_name(self):
        return self.firstname + " " + self.surname

    @classmethod
    def get_key_from_mail(cls, mail_address):
        key = mail_address.split("@")
        return key[0]


class Machine(Node):
    pass


class Process(Organization):
    """Control the flows of a full process """
    def __init__(self, actors):
        Organization.__init__(self, self.__class__.__name__, actors)
        self.executions = []

    def start(self, process_instance, customer):
        self.customer = customer
        movement = Movement(process_instance, customer)
        movement.launch(self)

        self.executions.append(movement)

    def assign(self, movement, actor_role):
        """Reasigns movement to a child"""
        node = self.nodes[actor_role]
        if movement in self.inbox:
            movement.launch(node)
