def readraw(typ=None):
    if type is None:
        return input().strip()
    else:
        return type(input().strip())


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    n = readraw(int)
    t, a = readarray(int)
    x = readarray()
    diff = [abs(t - e * 0.006 - a) for e in x]
    diff_min = min(diff)
    ans = diff.index(diff_min) + 1
    print(ans)
