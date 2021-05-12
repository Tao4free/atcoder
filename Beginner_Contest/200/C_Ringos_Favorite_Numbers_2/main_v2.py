from sys import stdin, stdout


def readstd():
    return stdin.readline().strip()


def readarray(typ):
    inpt_list = readstd().split()
    return [int(x) if x.isdigit() else x for x in inpt_list]


if __name__ == "__main__":
    num = int(readstd())

    arr = readarray(int)

    count = 0
    cur = 0
    nxt = 0
    while cur < len(arr) -1:
        nxt += 1
        if (arr[cur] - arr[nxt]) % 200 == 0:
            count += 1
        if nxt == len(arr) -1:
            cur += 1
            nxt = cur
    stdout.write(str(count))
