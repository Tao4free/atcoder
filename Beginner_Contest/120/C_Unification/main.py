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
    stack = readraw()
    key = '01'
    key_rev = '10'
    ans = 0
    while True:
        cnt = stack.count(key)
        cnt_rev = stack.count(key_rev)
        stack = stack.replace(key, '')
        ans += 2*cnt
        if cnt == 0:
            if cnt_rev == 0:
                break
            else:
                key = '10'
    print(ans)
