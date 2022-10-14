from src.num import Num
from src.sym import Sym
from src.data import Data
from src.row import Row
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
    print('\n:div', entropy, ':mid', mode)
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

    def mid(col):
        return col.mid()

    def div(col):
        return col.div()

    print("\nxmid", data.stats(2, data.cols.x, mid))
    print("xdiv", data.stats(3, data.cols.x, div))
    print("ymid", data.stats(2, data.cols.y, mid))
    print("ydiv", data.stats(3, data.cols.y, div))


def test_data_distance():
    data = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    between = data.dist(data.rows[0], data.rows[1])
    assert 0 <= between <= 1
    print("\n", sorted([round(data.dist(data.rows[0], row), 2) for row in data.rows]))


def test_around():
    data = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    around = data.around(data.rows[0])
    print('\nrow at index = 0 ', around[0].cells, "\n")
    for i in range(1, 380, 40):
        print(i, around[i].cells)
    return True


def test_nearest_neighbor():
    data = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    around = data.around(data.rows[0])
    k = [3, 5, 10]
    for x in k:
        print('k=', x, '\n', data.nearest_neighbor(around, x))

# FIX THIS
# takes the symbols seen in 5 nn and finds the most common symbol
def test_classifier():
    data = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    k = 5
    s = data.classifier(k)
    sym = Sym()
    for n in s:
        sym.add(n)
    mode = sym.mid()

    print('\nMost common symbol seen in k=5 is ', mode)


# regression for numerics
def test_regression():
    data = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    k = 5
    col_at = 4

    # report average acceleration of k = 5
    avg = data.predicted(k, col_at)
    print("\nAverage/Predicted Acc for k=5: ", avg)

    # report error of numeric variable
    mre = data.error(k, col_at)
    print("\nMagnitude relative error = ", mre)


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
    fail_count += test_data_distance()
    fail_count += test_around()
    fail_count += test_nearest_neighbor()
    fail_count += test_classifier()
    fail_count += test_regression()
    return fail_count  # 0 is Success


if __name__ == "__main__":
    main()
    
