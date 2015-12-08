# import pdb



class LogisticInspection:

    def __init__(self, responsible):
        self.responsible = responsible


class Qactivity:

    def __init__(self, responsible):
        self.responsible = responsible
        self.inputs = set()

    def add_input(self, nc_item):
        self.inputs.add(nc_item)

    def process_input(self, nc_item, failureState, qty=None):
        if nc_item not in self.inputs:
            self.add_input(nc_iterm)
        if qty is None:
            qty = nc_item.qty

        result = NcItem(nc_item.track, failureState, qty)
        nc_item.origin = result
        nc_item.source = self

    def close_input(self, nc_item, failureState):
        pass

    def lost_input(self, nc_iterm, failureState):
        pass


class Inspection(Qactivity):
    pass


class Detection(Qactivity):
    pass

