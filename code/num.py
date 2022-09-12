import re
import math
from code import settings
import random

class Num:
    # Object for Num class,
    def __init__(self, c=0, s=""):
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
            sorted(self._has.items())  # sort by key or value?
            self.isSorted = True
        return self._has

    #  Reservoir sampler - keeps N numbers and if you see more than N, some old number is replaced at random
    def add(self, v):
        if v != '?':
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < settings.the.nums:
                pos = 1 + len(self._has)
            elif random.random() < settings.the.nums / self.n:
                pos = random.randint(0, len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = int(v)

    def div(self):
        div_list = []
        a = self.nums()
        for v in a.values():
            div_list.append(v)
        mean = sum(div_list) / len(div_list)
        # measure of how data points differ from the mean
        variance = sum([((x - mean) ** 2) for x in div_list]) / len(div_list)
        return variance ** 0.5

    def mid(self):
        mid_list = []
        a = self.nums()
        for v in a.values():
            mid_list.append(v)
        len_of_list = len(mid_list)
        if len_of_list % 2 == 0:
            first_median = a[len_of_list // 2]
            second_median = a[len_of_list // 2 - 1]
            mid = (first_median + second_median) / 2
        else:
            mid = a[len_of_list // 2]
        return mid
