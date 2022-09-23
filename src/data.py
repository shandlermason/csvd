from src import settings
from src.row import Row
from src.cols import Cols
from src.num import Num
from src.sym import Sym


class Data:
    def __init__(self, src):
        rows_csv = settings.csv_function(src)
        self.cols = None  # summaries of data
        self.rows1 = {}
        self.rows = []

        for row in rows_csv:
            self.add(row)

    # add cell to appropriate column
    def add(self, xs):
        x = xs
        if self.cols is None:
            self.cols = Cols(xs)
            return True
            # self.rows.pop(0)


        row = Row(xs)
        self.rows.append(row)
        for _, col in self.cols.x.items():
            col.add(row.cells[col.at])
        for _, col in self.cols.y.items():
            col.add(row.cells[col.at])
            """
            col.add()
            for _, col in enumerate(todo):
                y = row.cells[col.at]
                col.add(row.cells[col.at])

        for ky, todo_x in self.cols.x.items():
            for r in xs:
                for c in r:
                    if r.index(c) == ky:
                        # row = Row(c)
                        row2 = Row(r)
                        todo_x.add(row2.cells)
                        # todo_x.add(row2)
        for ky, todo_y in self.cols.y.items():
            for r in xs:
                for c in r:
                    if r.index(c) == ky:
                        # row = Row(r)
                        row = Row(c)
                        todo_y.add(row.cells)
            """
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
        x = self.rows[1]
        x = row1.cells
        for _, col in self.cols.x.items():
            col.dist(row1.cells[col.at], row2.cells[col.at])

            if isinstance(col, Num):  # type check, if col is an instance of 'Num'
                for x, y in row1 and row2:
                    for c, d in x, y:
                        if x.index(c) == ky and y.index(d) == ky:
                            r1 = Row(c)
                            r2 = Row(d)
                            d = d + col.dist(r1.cells[col.at], r2.cells) ** settings.the['p']
        return (d/len(self.cols.x))**(1/settings.the['p'])

"""
    # find nearest neighbor for each row
    def around(self, row1):
        def fun(row2):
            row = row2
            dist = self.dist(row1, row2)
            return [row, dist]
        d = {"dist": fun(self.rows)}
        return sorted(d.items())
"""