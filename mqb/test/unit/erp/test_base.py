from mqb.domain.erp.base import (
                                 Resource,
                                 Node,
                                 Organization,
                                 Movement,
                                 Process
                                 )
from mqb.domain.erp.exceptions import IncorrectNodeClass
from freezegun import freeze_time
import datetime

import pytest
import pdb
import unittest


@pytest.mark.current
class A_Resource:

    def should_be_initialized_with_defaults(self):
        resource = Resource()

        assert not resource.key

    def should_be_inititalized_with_extra_parameters(self):
        resource = Resource("key")

        assert resource.key == "key"

@pytest.mark.current
class A_Node:

    def setup_method(self, method):
        self.key = "node key"

    def should_be_initialized_orphan_by_default(self):
        node = Node(self.key)

        assert not node.parent
        assert node.key == self.key


@pytest.mark.current
class An_Organization:

    def setup_method(self, method):
        self.key = "key"
        child_1 = Node("child1")
        child_2 = Node("child2")
        self.childs = {"role_1": child_1, "role_2": child_2}

    def should_be_initialized_with_defaults(self):
        organization = Organization(self.key)

        assert organization.key == self.key
        assert not organization.nodes
        assert not organization.parent

    def could_be_initialized_with_childs(self):

        organization = Organization("father",
                                    self.childs)

        assert len(organization.nodes) == 2
        assert self.childs["role_1"].parent == organization

    def should_add_and_remove_nodes(self):
        organization = Organization(self.key)

        child1 = "role_1"
        organization.add_node(self.childs[child1], child1)

        assert organization.nodes[child1] == self.childs[child1]

        organization.remove_node(child1)

        assert not organization.nodes


@pytest.mark.current
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


@pytest.mark.current
class A_Process:

    def setup_method(self, method):
        self.key = "key"
        self.process_request = Resource(self.key)

        self.customer = Node("customerKey")
        role_1 = Node("role1")
        role_2 = Node("role2")

        self.roles = {"role1": role_1, "role2": role_2}

    def should_be_initialized_with_defaults(self):
        process = Process(self.roles)

        assert process
        assert not process.executions
        assert len(process.nodes) == 2

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
