#!/usr/bin/env python3
from sys import stdin, stdout


def readstd():
    return stdin.readline().strip()


def readarray(typ):
    inpt_list = readstd().split()
    return list(map(typ, inpt_list))


def readmatrix(n):
    return [readstd() for _ in range(n)]


def bitexplore(n, arr):
    ans = 1 << 30
    for ptn in range(1 << n-1):
        ans_xor = 0
        ans_or = 0
        for i in range(n):
            ans_or |= arr[i]
            if ptn >> i & 1:
                ans_xor ^= ans_or
                ans_or = 0
        ans_xor ^= ans_or
        ans = min(ans, ans_xor)
    return ans


if __name__ == "__main__":
    n = int(readstd())
    arr = readarray(int)
    ans = bitexplore(n, arr)
    stdout.write(str(ans))
