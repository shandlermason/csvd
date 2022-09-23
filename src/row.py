import copy

class Row:
    def __init__(self, t=0):
        self.cells = t  # one record
        self.cooked = copy.deepcopy(t)  # copy function needs to be implemented
        self.isEvaled = False