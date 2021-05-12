#!/usr/bin/env python3
from sys import stdin, stdout
import operator as op
from line_profiler import LineProfiler


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
        # ans_or = op.or_(ans_or, arr[i])
        ans_or |= arr[i]
        if op.and_(op.rshift(ptn, i),  1):
            ans_xor = op.xor(ans_xor, ans_or)
            ans_or = 0
    ans_xor = op.xor(ans_xor, ans_or)
    return ans_xor


def bitexplore():
    ans = min(list(map(bitone, range(op.lshift(1, n-1)))))
    return ans


def main():
    global n, arr
    # n = int(readstd())
    # n = readarray(int)[0]
    n = int(stdin.readline())
    arr = readarray(int)
    ans = bitexplore()
    stdout.write(str(ans))


prof = LineProfiler()
func_list = [readstd, readarray, readmatrix, bitexplore, bitone, main]
for func in func_list:
    prof.add_function(func)
prof.runcall(main)
prof.print_stats()
