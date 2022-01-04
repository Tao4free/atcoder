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
    s = list(readraw())
    query = [readarray() for _ in range(m)]
    for q in query:
        split = s[q[0]-1:q[1]]

        ans = 0
        for idx in range(1, len(split)):
            cur = split[idx]
            pre = split[idx-1]
            if [pre, cur] == ['A', 'C']:
                ans += 1
        # print(''.join(s))
        # print(''.join(str(c) for c in cnt))
        print(ans)

        # for q in query:
            # split = cnt[q[0]-1:q[1]]
            # split[0] = 0
            # print(sum(split))
    # ans = max(cnt)
    # print(ans)
