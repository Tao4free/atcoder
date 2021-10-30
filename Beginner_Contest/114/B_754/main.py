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
    num = readraw()
    fix = 753
    ans = 10 ** 30
    for idx in range(2, len(num)):
        extract = num[idx-2:idx+1]
        subnum = int(extract)
        sub = abs(subnum - fix)
        if ans > sub:
            ans = sub
    print(ans)
