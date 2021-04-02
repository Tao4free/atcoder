#!/usr/bin/env python3

def get2num():
    raw = input().split(' ')
    out = [int(x) if x.isdigit() else x for x in raw]
    return out


h, v, x, y = get2num()
matrix = []
for i in range(h):
    matrix.append(input())

x -= 1
y -= 1

fix_row = matrix[x]
fix_col = ''.join([m[y] for m in matrix])

fix_row_lefter = fix_row[0:y][::-1]
fix_row_righter = fix_row[y+1:]
fix_col_upper = fix_col[0:x][::-1]
fix_col_lower = fix_col[x+1:]

strlist = [
    fix_row_lefter,
    fix_row_righter,
    fix_col_upper,
    fix_col_lower,
    ]

count = sum(
        [len(s.split('#')[0]) for s in strlist]
        ) + 1
print(count)
