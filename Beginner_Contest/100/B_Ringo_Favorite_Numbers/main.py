def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    knd, num = readarray()
    if num == 100:
        num += 1
    ans = int(str(num) + '00'*knd)
    print(ans)
