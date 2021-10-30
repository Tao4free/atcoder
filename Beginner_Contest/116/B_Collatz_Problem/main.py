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


def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


if __name__ == "__main__":
    num = readraw(int)
    pre = num
    cur = pre

    dic = {cur: 1}
    for idx in range(1000000):
        ans = idx + 2
        pre = cur
        cur = f(pre)
        if cur in dic:
            break
        else:
            dic[cur] = 1

    print(ans)
