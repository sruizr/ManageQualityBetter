from mqb.domain.erp.roles import Role


class A_Role:

    def should_be_initialized_with_defaults(self):
        node_key = "nodeKey"
        node = Node(node_key)
        role = Role(node)

        assert role
        assert role.decorated == node
        assert role.key == node.key + "@Role"
