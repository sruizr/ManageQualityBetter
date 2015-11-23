from mqb.domain.erp.base import (
                                 Resource,
                                 Node,
                                 WorkItem,
                                 Organization
                                 )
from mqb.domain.erp.exceptions import IncorrectNodeClass

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

    def could_be_initialized_with_organization_parent(self):
        node = Node(self.key)
        wrong_parent = Node("wrong parent key")
        parent = Organization("parent key")

        try:
            node = Node(self.key, wrong_parent)
            pytest.fail("No IncorrectNodeException is caught")
        except Exception:
            assert Exception

        node = Node(self.key, parent)
        assert node in parent.nodes
        assert node.parent == parent

@pytest.mark.current
class An_Organization:

    def setup_method(self, method):
        self.key = "key"

    def should_be_initialized_with_defaults(self):
        organization = Organization(self.key)

        assert organization.key == self.key
        assert organization.nodes
        assert not organization.parent

    def could_be_initialized_with_childs_and_parent(self):
        son = Node("son")
        daughter = Node("daughter")
        grandfather = Organization("grandfather")

        organization = Organization("father",
                                    [son, daughter], grandfather)

        assert organization.parent == grandfather
        assert organization.nodes
        assert organization.nodes[0].parent == organization


class A_Flow:

    def should_start(self):
        pytest.fail("Not-implemented")


class A_work_item:

    def should_be_created_at_node_outbox(self):
        node = Node()  # It's a root node. Example organization
        work_item = WorkItem(node)

        assert work_item.source == node

    def should_moves_from_source_outbox_node_to_destination_inbox_node(self):
        source = Node()
        destination = Node()

        work_item = WorkItem(source)
        source.launch(work_item, destination)

        assert(destination.inbox[destination.inbox.keys()[0]] == work_item)
        assert not source.outbox
        assert work_item.destination == destination

    def should_removes__at_a_node_inbox(self):
        pytest.fail("Not-Implemented")
