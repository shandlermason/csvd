from code.num import Num
from code.settings import oo, the


def test_the():  # do I need eg.the()?
    oo(the)
    return True


def test_num(num, mid, div):
    num = Num(0, '')
    for i in range(0, 100):
        num.add(i, i)
    mid, div = num.mid(), num.div()
    print(mid, div)
    assert (50 <= mid <= 52) and (30.5 < div < 32)

