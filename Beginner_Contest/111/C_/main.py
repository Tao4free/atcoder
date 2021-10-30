def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    num = int(readraw())
    arr = readarray()
    a = arr[::2]
    b = arr[1::2]
    a_set = set(a)
    b_set = set(b)
    if a_set == b_set:
        ans = num // 2
    else:
        ans = min(len(a_set) - 1, len(b_set) - 1,  len(a_set.union(b_set)) - 2)
    print(ans)
