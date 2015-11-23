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
        assert node._parent == parent

    def should_init_flow_at_outbox(self):
        resource = Resource()

    def should_launch_work_items_from_outbox_to_destination_inbox(self):
        pytest.fail("Not implemented")

    def should_pull_work_items_from_inbox(self):
        pytest.fail("Not implemented")

    def should_push_work_items_to_outbox(self):
        pytest.fail("Not implemented")


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


@pytest.mark.current
class A_work_item(Resource):

    def should_be_initialized_with_defaults(self):
        pytest.fail("Not implemented")

    def should_be_initialized_with_optionals(self):
        pytest.fail("Not implemented")


