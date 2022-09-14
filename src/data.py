import src.cols
from src import cols
from src import settings
from src.row import Row
from src.cols import Cols


class Data:
    def __init__(self, src):
        self.cols = None  # summaries of data
        self.rows = []

        for row in src:
            self.rows.append(row)
        self.add(self.rows)


        """
        for lst in src:
            self.cols = []
            val_list = []
            for val in lst:
                if type(val) == str:
                    self.cols.append(val)
                else:
                    self.rows.append(val)
        
           # tp = type(str_list)
            #self.add(str_list)
            self.add(self.cols)
            self.add(self.rows)
        """

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
        if self.cols is None:
            self.cols = Cols(xs[0])
        print(self.cols)



        """
        else:
            for row in self.rows:
                df = ''.join((f'{x:^7}' for x in row))
            print(df)
        
            #self.row +=1  # row = settings.push(self.rows, xs.cells and xs or Row(xs))
        """
        """for x, todo in {**self.cols.x, **self.cols.y}.items():
                todo.add(xs[todo.at])
        """

    def stats(self, places, showCols, fun,):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t = {}
        for x, col in showCols:
            v = fun(col)
            v = type(v) == "number" and settings.rnd(v, places) or v
            t[col] = v
        return t
