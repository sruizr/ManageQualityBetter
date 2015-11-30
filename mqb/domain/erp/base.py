from .exceptions import (
                         IncorrectNodeClass,
                         )
import datetime


class Resource:
    """Resources of the system"""
    def __init__(self, key=None):
        self.key = key
        self.id = None


class Material(Resource):

    def __init__(self, concept):
        Resource.__init__(self)
        self.concept = concept


class Concept(Resource):

    def __init__(self, key, description=None):
        Resource.__init__(self, key)
        self.description = description


class Information(Resource):

    def __init__(self, concept, template=None):
        Resource.__init__(self)
        self.concept = concept
        self.template = template


class Node(Resource):
    """Active resources of the system, they generate flows"""
    def __init__(self, key):
        """If parent is omited the node is a root node"""
        Resource.__init__(self, key)

        self._parent = None

        # Not checked yet
        self.inbox = {}
        self.on_process = {}
        self.outbox = {}
        self.log_area = {}
        self.tag = None
        self.location = None

    @property
    def parent(self):
        return self._parent

    def create_work_item(self, work_item, activity):
        key = "{}.{}/{}.{}".format(self.__class__, self._id,
                                   activity.__class__, activity._id)
        self.outbox[key] = work_item

    def transfer(self, key, source_area, destination_area):
        if source_area == 'input':
            work_item = self.input_area.pop(key)
        elif source_area == 'processing':
            work_item = self.processing_area.featpop(key)
        elif source_area == 'output':
            work_item = self.output_area.pop(key)
        else:
            return False
        if destination_area == 'input':  # rework!
            self.input_area[key] = work_item
        elif destination_area == 'processing':
            self.processing_area[key] = work_item
        elif destination_area == 'output':
            self.output_area[key] = work_item
        elif destination_area == 'log':  # log only receives, never sends
            self.log_area[key] = work_item
        else:
            return False
        return True

    @classmethod
    def move_work_item(self, key, source, destination):
        try:
            work_item = source.output_area.pop(key)
        except Exception:
            print(Exception)
        else:
            destination.input_area[key] = work_item

    def launch(self, key, destination):
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
                 surname=None, genre=None):
        Node.__init__(self, key)
        self.mail_address = mail_address
        self.firstname = firstname
        self.surname = surname
        self.genre = genre

    def full_name(self):
        return firstname + " " + surname

    @classmethod
    def get_key_from_mail(cls, mail_address):
        key = mail_address.split("@")
        return key[0]

class Machine(Node):
    pass


class Movement:
    """Movement of a resource from one node to other"""
    def __init__(self, resource, source, key=None, parent=None):
        """Movement is created from outbox of source"""
        self.source = source
        self.resource = resource
        self.begin = datetime.datetime.utcnow()
        if not key:
            key = source.key
        self.key = key

        source.outbox[self.key] = self

    def launch(self, destination):
        """It moves the resource from source oubox area to destination inbox
        area"""

        self.destination = destination
        self.shot = datetime.datetime.utcnow()

        self.destination.inbox[self.key] = self.source.outbox.pop(self.key)

    def close(self):
        """ The movement is not active, resource is consumed"""
        self.end = datetime.datetime.utcnow()
        del self.destination.inbox[self.key]


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

class Process_Request(Resource):
    pass
