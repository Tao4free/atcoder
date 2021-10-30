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
    a, b, k = readarray()
    test = max(a, b) + 1
    cnt = 0
    while True:
        test -= 1
        if (a % test == 0) and (b % test == 0):
            cnt += 1
            if cnt == k:
                ans = test
                break
    print(ans)
