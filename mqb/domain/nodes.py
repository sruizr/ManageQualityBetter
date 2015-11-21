from mqb.domain.base import Organization


class Customers(Organization):

    def __init__(self, customers=None):
        Organization.__init__(self, name="customers")
        if customers:
            self.customers = customers


class Customer(Organization):

    def __init__(self, name, mail_address, category, language="es"):
        self.name = name
        self.mail_address = mail_address
        self.category = category
        self.language = language

