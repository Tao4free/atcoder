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
    k = int(readraw())
    for n in range(1, k+1):
        if len(str(n)) == 1:
            ans = str(n)
        elif n == 10:
            ans = '19'
        else:
            ans = '9'
            lendigit = 1 if n <= 10 else int(str(n)[0]) + 1
            # print(lendigit)
            # print('len: ', lendigit)
            add = False
            for i in range(lendigit-1, 0, -1):
                # print('check: ', str(int(str(n)[i]) + 1)[-1])
                try:
                    ans += str(int(str(n)[i]) + 1)[-1]
                except:
                    add = True
            if int(str(n)[-1]) == 9 or add:
                ans += '1'
            ans = ans[::-1]
        print(ans)
