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


if __name__ == "__main__":
    n, k = readarray()

    tree = [readraw(int) for _ in range(n)]
    tree.sort()

    ans = min(tree[i+k-1] - tree[i] for i in range(n-k+1))
    print(ans)
