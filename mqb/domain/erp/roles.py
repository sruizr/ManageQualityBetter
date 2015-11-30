from .base imort Node


class Role(Node):

    def __init__(self, decorated):
        self.decorated = decorated
        Node.__init__(self, decorated.key + "@" + self.__class__.__name__)
