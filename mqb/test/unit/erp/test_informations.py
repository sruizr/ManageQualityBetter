from mqb.domain.erp.

class An_Information:

    def should_be_initialized_with_defaults(self):
        concept = Concept("itemKey")
        information = Information(concept)

        assert information
        assert information.concept == concept

    def could_be_initialized_with_template(self):
        concept = Concept("itemKey")
        template = "Plain template"
        information = Information(concept, template)

        assert information
        assert information.template == template
