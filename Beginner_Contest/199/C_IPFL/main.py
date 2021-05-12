from sys import stdin, stdout


def readstd():
    return stdin.readline().strip()


def readarray(typ):
    inpt_list = readstd().split()
    return list(map(typ, inpt_list))


def readmatrix(n_query):
    flip = False
    for _ in range(n_query):
        mode, a, b = readarray(int)
        a -= 1
        b -= 1
        if mode == 2:
            flip = not flip
        else:
            if flip:
                a = (a + n) % (2 * n)
                b = (b + n) % (2 * n)
            s[a], s[b] = s[b], s[a]
    if flip:
        s[n:], s[:n] = s[:n], s[n:]


if __name__ == "__main__":
    n = int(readstd())
    s = list(readstd())
    n_query = int(readstd())
    readmatrix(n_query)
    ans = ''.join(s)
    stdout.write(ans)
