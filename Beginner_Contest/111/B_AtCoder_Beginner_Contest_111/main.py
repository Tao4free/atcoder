def readraw():
    return input().strip()


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


if __name__ == "__main__":
    num_str = readraw()
    num_str_list = list('123456789')
    num = int(num_str)
    for n_str in num_str_list:
        new_str = n_str*3
        new_num = int(new_str)
        if new_num >= num:
            ans = new_num
            break
    print(ans)
