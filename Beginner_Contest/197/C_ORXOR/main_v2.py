from sys import stdin, stdout
import operator as op


def readstd():
    return stdin.readline().strip()


def readarray(typ):
    inpt_list = readstd().split()
    return list(map(typ, inpt_list))


def readmatrix(n):
    return [readstd() for _ in range(n)]


def bitexplore(n, arr):
    ans = oplshift(1, 30)
    for ptn in range(oplshift(1, n-1)):
        ans_xor = 0
        ans_or = 0
        for i in range(n):
            ans_or = opor_(ans_or, arr[i])
            if opand_(oprshift(ptn, i), 1):
                ans_xor = opxor(ans_xor, ans_or)
                ans_or = 0
        ans_xor = opxor(ans_xor, ans_or)
        ans = min(ans, ans_xor)
    return ans


if __name__ == "__main__":
    opxor = op.xor
    opor_ = op.or_
    opand_ = op.and_
    oplshift = op.lshift
    oprshift = op.rshift
    n = int(readstd())
    arr = readarray(int)
    ans = bitexplore(n, arr)
    stdout.write(str(ans))
