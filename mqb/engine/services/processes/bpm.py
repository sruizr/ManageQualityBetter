from mqb.domain.erp.base import Process
from mqb.domain.erp.nodes import Machine
from mqb.domain.erp.roles import Role
from pyactiviti import Activiti


class BpmProcess(Process):

    def __init__(self, activiti_auth, activiti_url):
        self.activiti_engine = Machine("activiti") # Node to store status of activiti_engine
        self.activiti = Activiti(activiti_url) # TODO: Manage authorization

    def refresh_activiti_engine(self, process_key=None):
        """Load & update executions inside activiti engine"""
        filter = {}
        if process_key:
            filter.update({"processDefinitionKey": process_key})

        executions = Execution.list(filter)


class BpmMapper:
    pass


class BpmEngine(Role):
    def __init__(self, machine):
        Role.__init__(self, machine)
        Activiti.


class Execution:
    pass


class Task:
    pass


class User:
    pass
