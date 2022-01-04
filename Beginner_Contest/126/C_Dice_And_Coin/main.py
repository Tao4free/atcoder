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
    n, b = readarray()

    ans = 0
    for i in range(1, n+1):
        ans_sub = 1
        score = i
        while score < b:
            score *= 2
            ans_sub *= 1/2
        ans += 1/n * ans_sub

    print(ans)
