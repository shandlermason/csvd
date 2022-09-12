from code.num import Num
from code import settings


# test if object exist
def test_the():
    if settings.the:
        return True
    else:
        print('the does not exist')


def test_num():
    num = Num()
    for i in range(0, 100):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid, div)
    assert (50 <= mid <= 52) and (30.5 < div < 32)


# executes each test and stores results at the end prints results and # of fails
def main():
    fail_count = 0
    fail_count += test_the()
    fail_count += test_num()
    return fail_count  # 0 is Success


if __name__ == "__main__":
    main()
