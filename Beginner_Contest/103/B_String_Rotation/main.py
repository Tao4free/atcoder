from collections import deque


def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    s = list(readraw())
    t = list(readraw())
    ds = deque(s)
    dt = deque(t)
    ans = 'No'
    for i in range(len(s)):
        ds.rotate(1)
        if ds == dt:
            ans = 'Yes'
    print(ans)
