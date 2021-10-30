from collections import Counter

def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    s = readraw()
    t = readraw()
    s_c = Counter(s)
    t_c = Counter(t)
    s_c_str = ''.join([str(x) for x in s_c.values()])
    t_c_str = ''.join([str(x) for x in t_c.values()])
    ans = 'Yes' if s_c_str == t_c_str else 'No'
    print(ans)
