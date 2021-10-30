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
    num = int(readraw())
    arr = readarray()
    sum_num = int((1 + num) * num / 2)
    sum_arr = int(sum(arr))
    diff = sum_arr - sum_num
    op = 0 if diff == 0 else abs(diff) / diff
    b = int((int(abs(diff) / num) + 1) * op)
    # print('nihao: ', abs(sum_num - sum_arr) / num, b)

    ans = 0
    for i, v in enumerate(arr, 1):
        # t = abs(v-b-i)
        # print(f'\tv: {v}, b: {b}, i: {i}, abs(v-b-i): {abs(v-b-i)}')
        ans += abs(v - i - b)
    # print(sum_num, sum_arr, b, ans)
    print(ans)
