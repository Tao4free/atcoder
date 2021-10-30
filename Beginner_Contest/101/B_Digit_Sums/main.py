def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    nstr = readraw()
    n = int(nstr)
    narr = [int(c) for c in nstr]
    if n % sum(narr) == 0:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)
