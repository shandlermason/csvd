from src import settings
from src.row import Row
from src.cols import Cols
from src.num import Num
from src.sym import Sym


class Data:
    def __init__(self, src):
        rows_csv = settings.csv_function(src)
        self.cols = None  # summaries of data
        self.rows = []

        for row in rows_csv:
            self.rows.append(row)
        self.add(self.rows)

    # add cell to appropriate column
    def add(self, xs):
        if self.cols is None:
            self.cols = Cols(xs[0])
            self.rows.pop(0)
        for ky, todo_x in self.cols.x.items():
            for r in xs:
                for c in r:
                    if r.index(c) == ky:
                        row = Row(c)
                        todo_x.add(row.cells)
        for ky, todo_y in self.cols.y.items():
            for r in xs:
                for c in r:
                    if r.index(c) == ky:
                        row = Row(c)
                        todo_y.add(row.cells)

    def stats(self, places, showCols, fun):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t = {}
        for ky, col in showCols.items():
            v = fun(col)
            if type(v) is float:
                v = settings.rnd(v, places)
            t[col.name] = v
        return t

    # distance between rows (returns 0..1). For unknown values, assume max distance.
    def dist(self, row1, row2):
        d = 0
        for ky, col in self.cols.x.items():
            if isinstance(col, Num):  # type check, if col is an instance of 'Num'
                for x, y in row1 and row2:
                    for c, d in x, y:
                        if x.index(c) == ky and y.index(d) == ky:
                            r1 = Row(c)
                            r2 = Row(d)
                            d = d + col.dist(r1.cells, r2.cells) ** settings.the['p']
        return (d/len(self.cols.x))**(1/settings.the['p'])
