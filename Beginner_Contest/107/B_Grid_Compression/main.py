def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


def readmatrix(n):
    return [list(map(int, list(readraw().replace('.', '1').replace('#', '0')))) for _ in range(n)]


if __name__ == "__main__":
    h, w = readarray()
    matrix = readmatrix(h)
    print(matrix)
    matrix_remove_rows = []
    for m in matrix:
        print(all(e == 1 for e in m))
        if not all(e == 1 for e in m):
            matrix_remove_rows.append(m)

    remove_icols = []
    matrix_remove_cols = []
    # for i_col in len(matrix_remove_rows[0]):
    for i_col in range(len(matrix[0])):
        col = [m[i_col] for m in matrix_remove_rows]
        if not all(e == 1 for e in m):
            remove_icols.append(i_col)
    print(remove_icols)
    # print(ans)
