import src.cols
from src import cols
from src import settings
from src.row import Row
from src.cols import Cols
from _collections import defaultdict


class Data:
    def __init__(self, src):
        self.cols = None  # summaries of data
        self.rows = []

        for row in src:
            self.rows.append(row)
        self.add(self.rows)

    # add row to Data
    def add(self, xs):
        if self.cols is None:
            self.cols = Cols(xs[0])
            self.rows.pop(0)
        # xs is 1 big list of many list excluding column headers
        for r in xs:
            for c in r:
                row = Row(c)
                o = row.cells


        self.cols.y[0].add(1)
