def readraw(typ=None):
    if type is None:
        return input().strip()
    else:
        return type(input().strip())


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    n, m = readarray(int)
    data = {}
    data_list = []
    for im in range(m):
        p, y = readarray()
        data_list.append([p, y])
        if p in data:
            data[p].append(y)
        else:
            data[p] = [y]

    ref = {k: sorted(v) for k, v in data.items()}

    for p, y in data_list:
        print(f'{p:06d}{ref[p].index(y)+1:06d}')
