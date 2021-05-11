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


#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < n; ++i)
using namespace std;



int main()
{
	int n;
    cin >> n;
    vector<int> arr(n);
    rep(i, n) cin >> arr[i];


	int cur = 0;
    int nxt = 0;
    int cnt = 0;
    while (cur < sizeof(arr)) {
        nxt += 1;
        if ((arr[cur] - arr[nxt]) % 200 == 0) {
            cnt++;
        if (nxt = sizeof(arr) - 1) {
            cur++;
            nxt = cur;
      cout << cnt << "\n";
    }
	return 0;
}
