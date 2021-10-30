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


def split(arr):
    new_arr = []
    temp = []
    has_zero = False
    for a in arr:
        if a != 0:
            temp.append(a)
        else:
            has_zero = True
            new_arr.append(temp)
            temp = []
            continue
    if new_arr == []:
        new_arr = temp
    if has_zero:
        new_arr.append(temp)
    return new_arr


def do(arr):
    for s in split(arr):
        smin = min(s)
        cnt['ans'] += smin
        new_s = [e - smin for e in s]
        do(new_s)
    # arr_min = min(arr)
    # if arr_min != 0:


if __name__ == "__main__":
    readraw()
    arr_org = readarray()
    cnt = {'ans':0}
    ans = 0
    print(cnt)
    # print(split(arr_org))
    # arr_str = ','.join([str(x) for x in arr_org])
    # print(arr_str)
