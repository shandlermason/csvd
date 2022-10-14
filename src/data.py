from src import settings
from src.row import Row
from src.cols import Cols
from src.sym import Sym

class Data:
    def __init__(self, src):
        self.cols = None  # summaries of data
        self.rows = []
        [self.add(row) for row in settings.csv_function(src)]

    # add cell to appropriate column
    def add(self, xs):
        if self.cols:
            row = Row(xs)
            self.rows.append(row)
            for _, col in self.cols.x.items():
                col.add(row.cells[col.at])
            for _, col in self.cols.y.items():
                col.add(row.cells[col.at])
        else:
            self.cols = Cols(xs)

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
        for _, col in self.cols.x.items():
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** 2  # settings.the['p']
        return (d/len(self.cols.x)) ** (1/2)  # regex must be fixed to work with: (1/settings.the['p'])

    # What is around? - tell me the 5 objects in the room around you and your distance to them
    # find nearest neighbor for each row
    def around(self, row1):
        # function that returns distance to 'row1'
        def fun(row2):  # compares the first row to itself
            dist = self.dist(row1, row2)
            return dist
        # return sorted `rows` by least to the greatest distance from `row1`
        return sorted(self.rows, key=fun)

    # exclude list in around at index = 0
    def nearest_neighbor(self, sorted_list_of_rows, k_val):
        # slice after element at index = 0
        knn = sorted_list_of_rows[1:]
        # find k nearest neighbors
        return [knn[i] for i in range(0, k_val)]

    '''find dist: row at index 0 to row to doublecheck - 
    [round(self.dist(self.rows[0], knn[i]), 2) for i in range(0, k_val)]'''

    # finds the symbols seen in 5 nearest neighbors
    def classifier(self, k_val):
        knn_for_val = self.nearest_neighbor(self.around(self.rows[0]), k_val)
        s_list = []
        for _, col in self.cols.all.items():
            if isinstance(col, Sym):
                for ro in knn_for_val:
                    s_list.append(ro.cells[col.at])
        return s_list

    # find average of 5 nearest neighbors in dependent column
    def predicted(self, k_val, col_loc):
        knn_for_val = self.nearest_neighbor(self.around(self.rows[0]), k_val)
        acc_list = []
        for row in knn_for_val:
            acc_list.append(row.cells[col_loc])
        return sum(acc_list) / len(acc_list)

    # find magnitude relative error
    def error(self, k_val, col_loc):
        # finds actual value in 6th nearest neighbor
        knn_val = self.nearest_neighbor(self.around(self.rows[0]), k_val+1)  # k=6
        actual = knn_val[k_val+1].cells[col_loc]  # column value in k=6

        # the predicted value is the average of the values of its k nearest neighbors
        predicted = self.predicted(5, 4)

        # magnitude relative error
        return abs(predicted - actual) / actual
