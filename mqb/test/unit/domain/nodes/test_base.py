from mqb.engine.domain.nodes.base import (
                                   Organization,
                                   Person,
                                   Machine,
                                   Role,
                                   Process,
                                   )
from mqb.engine.domain.base import Node, Resource


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


class A_Person:

    def should_be_initialized_with_defaults(self):
        person = Person("personKey")

        assert person

    def could_be_inititalized_with_other_information(self):
        person_key = "sruiz"
        firstname = "Salvador"
        surname = "Ruiz"
        mail_address = "sruiz@sruiz.es"
        genre = "m"
        language = "en"

        person = Person(person_key, mail_address, firstname,
                        surname, genre, language)

        assert person.mail_address == mail_address
        assert person.key == person_key
        assert person.firstname == firstname
        assert person.surname == surname
        assert person.genre == genre
        assert person.language == language

    def could_have_a_password(self):
        assert None, "Not implemented"


class A_Machine:

    def should_be_initialized_with_defaults(self):
        machine = Machine("machineKey")

        assert machine


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


class A_Role:

    def should_be_initializad(self):
        person = Person("username", "user@company.com",
                        fist)
        role = Role("role", person)

        assert
