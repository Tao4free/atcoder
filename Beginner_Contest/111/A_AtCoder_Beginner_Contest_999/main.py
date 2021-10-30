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
    ans = num_str.replace('1', 'one').replace('9', '1').replace('one', '9')
    print(ans)
