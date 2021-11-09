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
    string = list(readraw())
    base = ['A', 'C', 'G', 'T']
    cnt = [0] * len(string)
    cnt[0] = [0, 1][string[0] in base]
    for idx in range(1, len(string)):
        cur = string[idx]
        if string[idx] in base:
            cnt[idx] = max(cnt[idx-1] + 1, cnt[idx-1])

    ans = max(cnt)
    print(ans)
