def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


def get_num_divisor(n):
    res = 0
    for i in range(1, n+1):
        if n % i == 0:
            res += 1
    return res


if __name__ == "__main__":
    num = int(readraw())
    ans = 0
    for n in range(1, num+1):
        if n % 2 == 1:
            nd = get_num_divisor(n)
            # print(f'n = {n}, nd = {nd}, ans = {ans}')
            if nd == 8:
                ans = ans + 1
    print(ans)
