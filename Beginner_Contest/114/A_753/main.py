def readraw(typ=None):
    if type is None:
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
    num = readraw(int)
    arr = [7, 5, 3]
    if num in arr:
        ans = 'YES'
    else:
        ans = 'NO'
    print(ans)
