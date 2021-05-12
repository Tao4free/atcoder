from sys import stdin, stdout
import io
import os


def readfast():
    return ioread().decode().strip()


def readstd():
    return stdin.readline().strip()


def readarray(typ):
    inpt_list = readfast().split()
    return list(map(typ, inpt_list))


def readmatrix(n):
    return [readfast() for _ in range(n)]


def genstrlist(matrix, x, y, v):
    x -= 1
    y -= 1
    fix_row = matrix[x]
    fix_col = ''.join(matrix)[y::v]

    fix_row_lefter = fix_row[:y][::-1]
    fix_row_righter = fix_row[y+1:]
    fix_col_upper = fix_col[:x][::-1]
    fix_col_lower = fix_col[x+1:]

    return (
        fix_row_lefter,
        fix_row_righter,
        fix_col_upper,
        fix_col_lower,
        )


def count_visibility(strlist):
    return sum(
        map(lambda x: len(x.split('#')[0]), strlist)
        ) + 1


if __name__ == "__main__":
    ioread = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    h, v, x, y = readarray(int)
    matrix = readmatrix(h)
    strlist = genstrlist(matrix, x, y, v)
    count = count_visibility(strlist)
    stdout.write(str(count))
