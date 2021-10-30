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
    right_pos = s[0] == 'A' and s[1] != 'C' and s[-1] != 'C'
    right_count = (str(s).count('A') + str(s).count('C')) == 2
    scp = ''.join(s).replace('A', '').replace('C', '')
    is_lower = scp.islower()
    right_ans = right_pos and right_count and is_lower
    if right_ans:
        ans = 'AC'
    else:
        ans = 'WA'
    print(ans)
