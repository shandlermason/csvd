import math


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

    # mode - most common symbol
    def mid(self):
        most = -1
        for k, v in self._has.items():
            if v > most:
                mode, most = k, v
                return mode

    # entropy - symbols occurring at probability
    def div(self):
        def fun(p):
            return p * math.log(p, 2)
        e = 0
        for n in self._has.values():
            if n > 0:
                e = e - fun(n/self.n)
        return e

    # distance between two values
    def dist(self, v1, v2):
        if v1 == "?" and v2 == "?":  # ? = unknown
            return 1  # am I handling unknown values correctly? What if v1 = ? and v2 = known value?
        elif v1 == v2:  # same symbol
            return 0
        else:
            return 1  # different symbols
