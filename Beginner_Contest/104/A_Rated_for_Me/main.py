def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    r = int(readraw())
    if r < 1200:
        ans = 'ABC'
    elif r < 2800:
        ans = 'ARC'
    else:
        ans = 'AGC'
    print(ans)
