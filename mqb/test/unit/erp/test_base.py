import mqb.domain.erp.base as base

import pytest
import pdb
import unittest


class A_Node:

    def should_be_created_by_other_node(self):
        pytest.fail("Not-implemented")


class A_Flow:

    def should_start(self):
        pytest.fail("Not-implemented")


class A_work_item:

    def should_be_created_at_node_outbox(self):
        node = base.Node()  # It's a root node. Example organization
        work_item = base.WorkItem(node)

        assert node.
        assert work_item.source == node

    def should_moves_from_source_outbox_node_to_destination_inbox_node(self):
        source = base.Node()
        destination = base.Node()

        work_item = base.WorkItem(source)
        source.launch(work_item, destination)

        assert(destination.inbox[destination.inbox.keys()[0]] == work_item)
        assert not source.outbox
        assert work_item.destination == destination

    def should_removes__at_a_node_inbox(self):
        pytest.fail("Not-Implemented")
