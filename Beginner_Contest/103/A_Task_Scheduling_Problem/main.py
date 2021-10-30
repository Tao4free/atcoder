from itertools import permutations


def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    arr = readarray()
    ptn = permutations([0, 1, 2])
    ans = 10**10
    for p in list(ptn):
        i, j, k = p
        temp = abs(arr[i] - arr[j]) + abs(arr[j] - arr[k])
        if temp < ans:
            ans = temp
    print(ans)
