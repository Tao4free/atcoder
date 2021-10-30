def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    return [int(x) for x in inpt_list]
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    n, m, x, y = readarray()
    x_arr = readarray()
    y_arr = readarray()
    x_max = max(x_arr)
    y_min = min(y_arr)
    ans = 'War'
    for i in range(x_max+1, y_min+1):
        if x_max < i <= y_min and x < i <= y:
            ans = 'No War'
            break
    print(ans)
