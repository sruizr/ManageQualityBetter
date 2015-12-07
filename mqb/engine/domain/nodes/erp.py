from .base import Organization


class Customer(Organization):

    def __init__(self, key, contact_person,
                 category, language="es"):
        Role.__init__(self, key, contact_person)

        self.key = key
        self.category = category

    @property
    def contact(self):
        return self.decorated


