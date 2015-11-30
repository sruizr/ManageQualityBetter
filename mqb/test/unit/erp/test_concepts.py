
class A_Concept:

    def should_be_initialized_with_defaults(self):
        concept = Concept("itemKey")

        assert concept
        assert concept.key == "itemKey"
        assert hasattr(concept, "description")

class A_Part:

    def setup_method(self, method):
        self.part_number = "part_key"
        self.description = "any description"

    def should_be_initialized_as_default(self):

        part = resources.Part(self.part_number)

        assert part.number == self.part_number

    def should_be_intitalized_with_description(self):
        part = resources.Part(self.part_number, self.description)

        assert part.description == self.description

