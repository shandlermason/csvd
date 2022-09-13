import re
from src.num import Num
from src.sym import Sym


class Cols:
    def __init__(self, names):
        self.names = names  # all the column names
        self.all = {}  # all the columns
        self.klass = None
        self.x = {}  # independent columns
        self.y = {}  # dependent columns, has symbols

        # iterate over names and return number asscoaited with name
        for c, s in enumerate(names):

            skipped_columns = re.findall(":$", s)  # checks if column header ends in colon

            if re.findall("[A-Z]", s):  # checks if column header starts with capital letter then Num
                col = Num(c, s)
                self.all[c] = col
                if not skipped_columns:
                    if re.findall("[!+-]", s):
                        self.y[c] = col  # dependent columns (have symbols)
                    else:
                        self.x[c] = col  # independent columns (no symbols)
            else:
                col = Sym(c, s)
                self.all[c] = col
                if not skipped_columns:
                    if re.findall("[!+-]", s):
                        self.y[c] = col  # dependent columns (have symbols)
                    else:
                        self.x[c] = col  # independent columns (no symbols)

            # not sure if this is in the right spot
            if re.findall("!$", s):
                self.klass = col
