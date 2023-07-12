from collections.abc import MutableMapping
from MatrixDict import MatrixDict
from Matrix import BaseDict

def main():
    m1 = MatrixDict(3, 3, 2)
    m2 = MatrixDict(3, 3, 4)
    m1[1,3] = 5
    m1[2,2] = 10
    m2[2,3] = 15
    m2[3, 3] = 7
    m3 = m1 * m2
    m4 = m1 + m2
    print(m3)
    print(m4)
    print(BaseDict.__abstractmethods__)
    # print(m3.items())
    # print(m1[2,3])
    # obj[5,3] = 55
    # print(m2[3,3])

if __name__ == '__main__':
    main()