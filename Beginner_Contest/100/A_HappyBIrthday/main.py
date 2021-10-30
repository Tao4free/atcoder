def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    a, b = readarray()
    if a + b <= 16 and a <= 8 and b <= 8:
        ans = 'Yay!'
    else:
        ans = ':('
    print(ans)
