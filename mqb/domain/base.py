class Node:
    """Active classes were operations are done"""
    def __init__(self):
        self.input_area = {}
        self.processing_area = {}
        self.output_area = {}
        self.log_area = {}
        self.tag = None
        self.location = None

    def transfer(self, key, source_area, destination_area):
        if source_area == 'input':
            resource = self.input_area.pop(key)
        elif source_area == 'processing':
            resource = self.processing_area.pop(key)
        elif source_area == 'output':
            resource = self.output_area.pop(key)
        else:
            return False
        if destination_area == 'input':  # rework!
            self.input_area[key] = resource
        elif destination_area == 'processing':
            self.processing_area[key] = resource
        elif destination_area == 'output':
            self.output_area[key] = resource
        elif destination_area == 'log':  # log only receives, never sends
            self.log_area[key] = resource
        else:
            return False
        return True

    @classmethod
    def move_resource(self, key, source, destination):
        try:
            resource = source.output_area.pop(key)
        except error:
            print(error)
        else:
            destination.input_area[key] = resource


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


class Resource:
    pass


class WorkItem:
    """It's a instance of Resource"""
    def __init__(self, resource, qty=1, tracking=None):
        self.resource = resource
        if tracking:
            self.tracking = tracking
        self.qty = qty




class Container(WorkItem):

    def __init__(self, name=None):
        self.workItems = []

class Tracking:
    """Groups resources with same origin"""
    def __init__(self, key):
        self.work_items = []
        self.key = key

    def add_work_item(self, work_item):


class Movement:
    """Create, destroy & moves work_items between nodes"""
    def __init__(self, node, work_item, source, destination):
        self.pass

    def moves(self, work_iterm, source, destination, actor=destination, process=None ):
        pass


class Process(Movement):
    """List of methods for movements """
    def __init__(self, name = None):
        self.movements = []



class
