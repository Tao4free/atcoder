from sys import stdin, stdout
import math


def readstd():
    return stdin.readline().strip()


def readarray(typ):
    inpt_list = readstd().split()
    return list(map(typ, inpt_list))


if __name__ == "__main__":
    year = int(input())
    print(math.ceil(year/100))
