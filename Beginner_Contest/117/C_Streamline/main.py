def readraw(typ=None):
    if typ is None:
        return input().strip()
    else:
        return typ(input().strip())


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.lstrip("-").isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    n, m = readarray()
    arr = readarray()
    print(sorted(arr))
    print(max(arr) - min(arr))
    ans = ""
    print(ans)
