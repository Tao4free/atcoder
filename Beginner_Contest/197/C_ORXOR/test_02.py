n = int(input())


def get_common(num):
    if num == 1:
        return sum([1])
    return sum([i for i in range(1, int(num/2)+1) if num % i == 0] + [num])

cashe = {}
def cal(num):
    for i in range(1, num+1):
        temp = cashe.get(i, None)
        if temp is None:
            temp = get_common(i)
        if not i in cashe:
            cashe[i] = temp

cal(n)
print(sum(cashe.values()))
