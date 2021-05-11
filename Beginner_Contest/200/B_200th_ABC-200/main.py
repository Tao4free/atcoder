from sys import stdin, stdout


def readstd():
    return stdin.readline().strip()


def readarray(typ):
    inpt_list = readstd().split()
    return list(map(typ, inpt_list))


if __name__ == "__main__":
    num, loop = map(int, input().split())

    for n in range(loop):
        if num % 200 == 0:
            num = int(num / 200)
        else:
            num = int(''.join([str(num), '200']))
    print(num)
