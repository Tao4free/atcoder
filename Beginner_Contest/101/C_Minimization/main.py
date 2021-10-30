import math

def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    n, k = readarray()
    l = n - k
    if l == 0:
        ans = 1
    else:
        ans = 1 + math.ceil(l/(k-1))
    print(ans)
