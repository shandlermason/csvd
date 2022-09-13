from src.num import Num
from src.sym import Sym
from src.data import Data
from src import settings
import codecs
from contextlib import closing
import csv
import requests
from collections import OrderedDict


# test if object exist
def test_the():
    if settings.the:
        return True
    else:
        print('the does not exist')


# median and standard deviation test
def test_num():
    num = Num()
    for i in range(1, 101):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid, div)
    assert (50 <= mid <= 52) and (30.5 < div < 32)


# what is the purpose of this test? Do I have to print numbers out even if test passes?
def test_bignum():
    num = Num()
    settings.the['nums'] = 32
    for i in range(1, 1001):
        num.add(i)
    assert 32 == len(num._has)


# testing Sym mode and entropy
def test_sym():
    sym = Sym()
    for x in {'1': "a", '2': "a", '3': "a", '4': "a", '5': "b", '6': "b", '7': "c"}.values():
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    # entropy = (1000 * entropy) // (1/1000)
    assert mode == "a" and 1.37 <= entropy <= 1.38


# test if we can read csv files
def test_csv():
    # myd = OrderedDict()
    row_list = []
    url = 'https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv'
    with closing(requests.get(url, stream=True)) as r:
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
        for row in reader:
            row_list.append(row)
        return row_list  # do not return this
        # iterate over ever item in list and convert to data type
        # call coerce for each cell in row_list then return list of list of mixed values



        # use the first row to initialize the ordered dictionary keys
        # myd[row_list[0][0]] = []

# test if csv file loads into Data
def test_data():
    d = Data(test_csv())
    assert d.cols != None
    """
    d = Data(test_csv())
    if d.cols.y:
        print('data columns y:', d.cols.y)
    """
    return True


# executes each test and stores results at the end prints results and # of fails
def main():
    fail_count = 0
    fail_count += test_the()
    fail_count += test_num()
    fail_count += test_bignum()
    fail_count += test_sym()
    fail_count += test_csv()
    fail_count += test_data()
    return fail_count  # 0 is Success


if __name__ == "__main__":
    main()
