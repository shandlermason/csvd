import re
from src import settings
import random


class Num:
    # Object for Num class,
    def __init__(self, c=0, s=""):
        self.n = 0  # items seen
        self.at = c or 0  # column position
        self.name = s or ""  # column name
        self._has = [float('inf')] * int(settings.the['nums'])  # kept data, list with fixed # of positions
        self.lo = float('inf')  # lowest seen
        self.hi = float('-inf')  # highest seen
        self.isSorted = True
        self.w = -1 if re.findall('-$', s or "") else 1  # what does 'w' stand for?

    #  Return sorted kept numbers
    def nums(self):
        if not self.isSorted:
            self._has = sorted(self._has)  # sort by value
            self.isSorted = True
        return self._has

    #  Reservoir sampler - keeps N numbers and if you see more than N, some old number is replaced at random
    def add(self, v):
        if v != '?':
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            pos = -1
            for i, val in enumerate(self._has):
                if val == float('inf'):
                    pos = i
                    break
            # if resevior sampler is full add number at random position based on percentage
            if pos == -1 and random.random() < int(settings.the['nums']) / self.n:
                pos = random.randint(0, len(self._has)-1)
            if pos != -1:
                self.isSorted = False
                self._has[pos] = int(v)

    def div(self):
        div_list = []
        for num in self._has:
            if num != float('inf'):
                div_list.append(num)

        perc_index_90 = (90/100) * len(div_list)
        perc_index_10 = (10/100) * len(div_list)
        return (div_list[int(perc_index_90)] - div_list[int(perc_index_10)])/2.58

    def mid(self):
        mid_list = []
        for num in self._has:
            if num != float('inf'):
                mid_list.append(num)

        len_of_list = len(mid_list)
        if len_of_list % 2 == 0:
            first_median = mid_list[len_of_list // 2]
            second_median = mid_list[len_of_list // 2 - 1]
            mid = (first_median + second_median) / 2
        else:
            mid = mid_list[len_of_list // 2]
        return mid

    # Normalized numbers 0..1. Everything else normalizes to itself.
    # Why? - can compare rocket speed to shoe size, change from comparing apples and oranges to apples and apples
    def norm(self, n):
        if n == '?':
            return n
        else:
            return (n-self.lo) / (self.hi-self.lo + 10 ** -32)

    # distance between 2 values
    def dist(self, v1, v2):
        if v1 == '?' and v2 == '?':
            return 1
        v1, v2 = self.norm(v1), self.norm(v2)
        if v1 == '?':
            if v2 < 0.5:  # if ???v1??? is unknown normalize to ???v2???
                return 0
            else:
                return 1
        if v2 == '?':
            if v1 < 0.5:
                return 0
            else:
                return 1
        return abs(v1-v2)
