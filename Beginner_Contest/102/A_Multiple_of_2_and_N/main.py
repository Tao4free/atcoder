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
    if num % 2 != 0:
        ans = num * 2
    else:
        ans = num
    print(ans)
