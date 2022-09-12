from src.num import Num
from src import settings


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




# executes each test and stores results at the end prints results and # of fails
def main():
    fail_count = 0
    fail_count += test_the()
    fail_count += test_num()
    return fail_count  # 0 is Success


if __name__ == "__main__":
    main()
