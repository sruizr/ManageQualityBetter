from mqb.engine.domain.base import (
                                 Resource,
                                 Node,
                                 Organization,
                                 Movement,
                                 Process,
                                 Material,
                                 Information,
                                 Concept,
                                 Person,
                                 Machine,
                                 )
from mqb.engine.exceptions import IncorrectNodeClass
from freezegun import freeze_time
import datetime


class A_Resource:

    def should_be_initialized_with_defaults(self):
        resource = Resource()

        assert not resource.key
        assert hasattr(resource, "id")

    def should_be_inititalized_with_extra_parameters(self):
        resource = Resource("key")

        assert resource.key == "key"


class A_Node:

    def setup_method(self, method):
        self.key = "node key"

    def should_be_initialized_orphan_by_default(self):
        node = Node(self.key)

        assert not node.parent
        assert node.key == self.key


class A_Movement:

    def setup_method(self, method):
        self.date = datetime.datetime(2000, 1, 1)
        self.source = Node("source key")
        self.destination = Node("destination key")
        self.resource = Resource()
        self.key = "mov key"

    @freeze_time("2000-1-1")
    def should_be_initialized_with_defaults(self):
        movement = Movement(self.resource, self.source)

        assert movement
        assert movement.resource == self.resource
        assert movement.source == self.source
        assert movement.begin == self.date

        # TODO: keys in inbox/outbox should be  improved with meaning
        assert movement == self.source.outbox[self.source.key]

    @freeze_time("2000-1-1")
    def could_be_initialized_with_key_and_parent(self):
        movement = Movement(self.resource, self.source, self.key)

        # TODO: link to parent
        assert movement
        assert movement.resource == self.resource
        assert movement.source == self.source
        assert movement.begin == self.date
        assert movement.key == self.key

    @freeze_time("2000-1-1")
    def should_be_launch_to_destination(self):

        movement = Movement(self.resource, self.source, self.key)
        movement.launch(self.destination)

        assert movement.destination == self.destination
        assert movement.shot == self.date
        assert self.destination.inbox[self.key] == movement
        assert not self.source.outbox

    @freeze_time("2000-1-1")
    def should_be_closed(self):
        movement = Movement(self.resource, self.source, self.key)
        movement.launch(self.destination)
        movement.close()

        assert not self.destination.inbox
        assert movement.end == self.date

    def should_start_with_an_initial_request(self):

        process = Process(self.roles)
        process.start(self.process_request, self.customer)

        assert process.inbox
        assert process.customer == self.customer
        assert process.executions[0].source == self.customer
        assert process.executions[0].destination == process

    def should_assign_resource_to_child_node(self):
        process = Process(self.roles)
        process.start(self.process_request, self.customer)
        process.assign(process.executions[0], "role1")

        assert not self.roles["role1"].inbox
        assert process.inbox


class A_Concept:

    def should_be_initialized_with_defaults(self):
        concept = Concept("itemKey")

        assert concept
        assert concept.key == "itemKey"
        assert hasattr(concept, "description")


class A_Material:

    def should_be_initialized_with_defaults(self):
        concept = Concept("itemKey")
        material = Material(concept)

        assert material
        assert material.concept == concept


class An_Information:

    def should_be_initialized_with_defaults(self):
        concept = Concept("itemKey")
        information = Information(concept)

        assert information
        assert information.concept == concept

    def could_be_initialized_with_template(self):
        concept = Concept("itemKey")
        template = "Plain template"
        information = Information(concept, template)

        assert information
        assert information.template == template


