from .exceptions import (
                         IncorrectNodeClass,
                         )

class Resource:
    """Resources of the system"""
    def __init__(self, key=None):
        self.key = key


class Node(Resource):
    """Active resources of the system, they generate flows"""
    def __init__(self, key, parent=None):
        """If parent is omited the node is a root node"""
        Resource.__init__(self, key)

        self._parent = parent
        if parent:
            if not issubclass(type(parent), Organization):
                raise IncorrectNodeClass
            if self not in parent.nodes:
                parent.nodes.append(self)

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

    @parent.setter
    def parent(self, value):
        if value:
            self._parent = value
            if self not in value.nodes:
                value.nodes.append(self)

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
    def __init__(self, key, nodes=[], parent=None):
        Node.__init__(self, key, parent)
        self.nodes = nodes
        for node in self.nodes:
            node.parent = self

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass


class WorkItem(Resource):
    def __init__(self, source):
        source.create_work_item(self)
        self.source = source


class Flow:
    "It's a movement of resource"
    def __init__(self, source):
        self.source = source

    def start(self, resource):
        """Resource is created in outbox of source node"""
        self.resource = resource

    def push(self, qty=1):
        """It sends a qty to a created resource to source outbox node"""
        pass

    def launch(self, destination):
        """It moves the resource from source oubox area to destination inbox
        area"""

    def pull(self, qty=None):
        """It picks a qty of resource from destination inbox area to
        on_progres area """

    def close(self):
        """ The flow is not active, all qty is consumed in destination inbox
        area"""


class Tracking:
    """Groups resources with same origin"""
    def __init__(self, key):
        self.work_items = []
        self.key = key

    def add_work_item(self, work_item):
        self.work_items.append(work_item)
        work_item.tracking = self


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
