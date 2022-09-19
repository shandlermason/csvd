from src.num import Num
from src.sym import Sym
from src.data import Data
from src import settings


# test if object exist
def test_the():
    if settings.the:
        print('\n', settings.the)
        return True
    else:
        print('the does not exist')


# median and standard deviation test
def test_num():
    num = Num()
    for i in range(1, 101):
        num.add(i)
    mid, div = num.mid(), num.div()
    print('\n', mid, '    ', div)
    assert (50 <= mid <= 52) and (30.5 < div < 32)


# what is the purpose of this test? Do I have to print numbers out even if test passes?
def test_bignum():
    num = Num()
    settings.the['nums'] = 32
    for i in range(1, 1001):
        num.add(i)
    print('\n', num.nums())
    assert 32 == len(num._has)
    settings.the['nums'] = 512


# testing Sym mode and entropy
def test_sym():
    sym = Sym()
    for x in {'1': "a", '2': "a", '3': "a", '4': "a", '5': "b", '6': "b", '7': "c"}.values():
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    print('\n', ':div', entropy, ':mid', mode)
    assert mode == "a" and 1.37 <= entropy <= 1.38


# test if we can read csv files
def test_csv():
    rows = settings.csv_function('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    print('\n')
    for line in rows[0:10]:
        print(line)
    assert len(rows) != 0


# test if csv file loads into Data
def test_data():
    d = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    print('\n')
    for col in d.cols.y:
        dd = d.cols.y[col].__dict__
        print(':at', dd['at'], ':hi', dd['hi'], ':isSorted', dd['isSorted'], ':lo', dd['lo'], ':n', dd['n'],
              ':name', dd['name'], ':w', dd['w'])
    assert d.cols.y is not None


def test_stats():
    data = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    """for col in data.cols.x:
        vals = data.cols.x[col]._has.values()
        md = Num.mid(vals) or Sym.mid(vals)
    """
    mid = lambda col: Num.mid(col)
    div = lambda col: Num.div(col)
    print('\n')
    """
    print("xmid", data.stats(2, data.cols.x, mid))
    print("xdiv", data.stats(3, data.cols.x, div))
    """
    print("ymid", data.stats(2, data.cols.y, mid))
    print("ydiv", data.stats(3, data.cols.y, div))


# executes each test and stores results at the end prints results and # of fails
def main():
    fail_count = 0
    fail_count += test_the()
    fail_count += test_num()
    fail_count += test_bignum()
    fail_count += test_sym()
    fail_count += test_csv()
    fail_count += test_data()
    fail_count += test_stats()
    return fail_count  # 0 is Success


if __name__ == "__main__":
    main()
    
