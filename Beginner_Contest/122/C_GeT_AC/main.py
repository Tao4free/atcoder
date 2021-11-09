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
    n, m = readarray()
    string = list(readraw())
    query = [readarray() for _ in range(m)]

    cnt = [0] * n
    cnt[0] = 0
    for idx in range(1, n):
        cur = string[idx]
        pre = string[idx-1]
        cnt[idx] = cnt[idx-1] + (1 if pre+cur == 'AC' else 0)

    for q in query:
        ans = cnt[q[1]-1] - cnt[q[0]-1]
        print(ans)
