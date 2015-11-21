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

class NodeDecorator(Node):

    def __init__(self, decorated):
        self.decorated = decorated

    def transfer(self):
        pass

    def move_work_item(self):
        pass


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
        self.work_items.append(work_item)
        work_item.tracking = self


class Flow:
    """Create, destroy & moves work_items between nodes"""

    def __init__(self, node, work_item, source, destination):
        self.source = source
        self.destination = destination
        self.node = node
        self.work_item = work_item

    def moves(self, work_item, source, destination, actor, process=None):
        pass


class Activity:

    def __init(self, id):
        self.id = id
        self.flows = []
        self.name = None
        self.start_date = None
        self.end_date = None
        self.parent = None

    def start(self, origin, in_flows):
        pass

    def process(self, origin, method):
        pass

    def launch_work_items(self, origin, out_flows, method):
        pass

    def end(self, origin, movements):
        pass


class Process(Activity):
    """List of methods for movements """
    def __init__(self, id, name=None):
        self.id = id
        if name:
            self.name = name
        self.active_activities = {}


