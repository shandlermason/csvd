class Sym:
    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c  # column position
        self.name = s  # column name
        self._has = {}

    # add one thing to column
    def add(self, v):
        if v != "?":
            self.n = self.n + 1
            if v in self._has:
                self._has[v] += 1
            else:
                self._has[v] = 1
