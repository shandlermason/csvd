from cols import Cols
import settings
from row import Row


class Data:
    def __init__(self, src):
        self.cols = None  # summaries of data
        self.rows = {}
        if type(src) == "string":
            for row in src:
                self.add(row)
        else:
            for k, row in src.items():
                self.add(row)

    # add row to Data
    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = settings.push(self.rows, xs.cells and xs or Row(xs))
            for x, todo in {self.cols.x, self.cols.y}:
                for y, col in todo.values():
                    col.add(row.cells[col.at])
