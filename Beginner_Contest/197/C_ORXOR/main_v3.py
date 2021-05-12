#!/usr/bin/env python3
from sys import stdin, stdout
import operator as op


def readstd():
    return stdin.readline().strip()


def readarray(typ):
    inpt_list = readstd().split()
    return list(map(typ, inpt_list))


def readmatrix(n):
    return [readstd() for _ in range(n)]


def bitone(ptn):
    ans_xor = 0
    ans_or = 0
    for i in range(n):
        ans_or = op.or_(ans_or, arr[i])
        if op.and_(op.rshift(ptn, i),  1):
            ans_xor = op.xor(ans_xor, ans_or)
            ans_or = 0
    ans_xor = op.xor(ans_xor, ans_or)
    return ans_xor


def bitexplore():
    ans = min(list(map(bitone, range(op.lshift(1, n-1)))))
    return ans


if __name__ == "__main__":
    n = int(readstd())
    arr = readarray(int)
    ans = bitexplore()
    stdout.write(str(ans))
