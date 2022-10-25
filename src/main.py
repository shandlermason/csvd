from src.data import Data

'''
def main():
    d = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')

    for col in d.train.y:
        dd = d.train.y[col].__dict__
        print(':at', dd['at'], ':hi', dd['hi'], ':isSorted', dd['isSorted'], ':lo', dd['lo'], ':n', dd['n'],
              ':name', dd['name'], ':w', dd['w'])
    print("\n")
    for col in d.test.y:
        dd = d.test.y[col].__dict__
        print(':at', dd['at'], ':hi', dd['hi'], ':isSorted', dd['isSorted'], ':lo', dd['lo'], ':n', dd['n'],
              ':name', dd['name'], ':w', dd['w'])

    print("\n", d.nearest_neighbor(5, "train"))
    print("\n", d.nearest_neighbor(5, "test"))


if __name__ == "__main__":
    main()
'''