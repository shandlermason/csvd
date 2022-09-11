import re
import misc
import math


class Num:
    # Object for Num class,
    def __init__(self, c, s):
        self.n = 0  # items seen
        self.at = c or 0  # column position
        self.name = s or ""  # column name
        self._has = {}  # kept data
        self.lo = float('inf')  # lowest seen
        self.hi = float('-inf')  # highest seen
        self.isSorted = True
        self.w = -1 if re.findall('-$', s or "") else 1  # what does 'w' stand for?

    #  Return sorted kept numbers
    def nums(self):
        if not self.isSorted:
            self._has.sort()
            self.isSorted = True
        return self._has

    #  Reservoir sampler - keeps N numbers and if you see more than N, some old number is replaced at random
    def add(self, v, pos):
        if v != '?':
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < misc.the.nums:
                pos = 1 + len(self._has)
            elif math.random() < misc.the.nums / self.n:
                pos = math.random(len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = int(v)
                