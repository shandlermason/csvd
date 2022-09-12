from src.num import Num
from src.sym import Sym
from src.data import Data
from src import settings
import csv


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
def csv():
    with open('./data/auto93.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)



# executes each test and stores results at the end prints results and # of fails
def main():
    fail_count = 0
    fail_count += test_the()
    fail_count += test_num()
    fail_count += test_bignum()
    fail_count += test_sym()
    return fail_count  # 0 is Success


if __name__ == "__main__":
    main()
