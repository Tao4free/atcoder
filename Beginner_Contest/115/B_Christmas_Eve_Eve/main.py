def readraw(typ=None):
    if typ is None:
        return input().strip()
    else:
        return typ(input().strip())


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    n = readraw(int)
    ps = [readraw(int) for _ in range(n)]
    m = max(ps)
    midx = ps.index(m)
    ps.pop(midx)
    ans = m // 2 + sum(ps)
    print(ans)
