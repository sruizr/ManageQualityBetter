class Node:
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
            resource |should| be_instance_of(Resource)
        except KeyError:
            raise KeyError('Resource with key %s not found in source node output area' % key)
        except ShouldNotSatisfied:
            source.output_area[key] = resource  # put it back in the source
            raise ContractError('Resource instance expected, instead %s passed' % type(resource))
        else:
            destination.input_area[key] = resource


class Person(Node):
    def __init__(self, name):
        Node.__init__(self)
        self.name = name
        self.mail_address = None
        self.full_name = None


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


class WorkItem(Resource):

    def __init__(self, tracking=None):
        Resource.__init__(self)
        self.tracking = tracking

class Amount(WorkItem):

    def __init__(self, tracking=None, qty=1):
        WorkItem.__init__(self, tracking, qty)
        self.qty = qty

class Container(Resource):

    def __init__(self, name=None):
        self.resources = []


class Movement:

    def __init__(self, node, resource, source, destination):
        self.pass


class Process(Movement):

    def __init__(self, name = None):
        self.movements = []



class
