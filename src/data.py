from src import cols
from src import settings
from src.row import Row
from src.cols import Cols


class Data:
    def __init__(self, src):
        self.cols = None  # summaries of data
        self.rows = {}
        for lst in src:
            str_list = []
            val_list = []
            for val in lst:
                if type(val) == str:
                    str_list.append(val)
                else:
                    val_list.append(val)

            self.add(str_list)
            self.add(val)


        """
        tp = print(type(src))
        if type(src) == "str":
            for row in src:
                self.add(row)
        else:
            for row in src:
                self.add(row)
        """

    # add row to Data
    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            # self.row +=1  # row = settings.push(self.rows, xs.cells and xs or Row(xs))
            for x, todo in {**self.cols.x, **self.cols.y}.items():
                todo.add(xs[todo.at])

    def stats(self, places, showCols, fun,):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t = {}
        for x, col in showCols:
            v = fun(col)
            v = type(v) == "number" and settings.rnd(v, places) or v
            t[col] = v
        return t
