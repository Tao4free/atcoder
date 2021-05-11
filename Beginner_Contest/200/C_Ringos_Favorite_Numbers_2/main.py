from sys import stdin, stdout


def readstd():
    return stdin.readline().strip()


def readarray(typ):
    inpt_list = readstd().split()
    return list(map(typ, inpt_list))


if __name__ == "__main__":
    num = int(readstd())

    arr = readarray(int)

    count = 0
    for cur in range(len(arr)):
        for next in range(cur+1, len(arr)):
            if (arr[cur] - arr[next]) % 200 == 0:
                count += 1
    stdout.write(str(count))
