def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    s = readraw()
    k = int(readraw())
    ans = '1'
    for i in range(0, min(len(s), k)):
        if s[i] != '1':
            ans = s[i]
            break
    print(ans)
