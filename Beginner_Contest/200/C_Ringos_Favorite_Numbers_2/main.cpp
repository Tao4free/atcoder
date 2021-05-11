#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < n; ++i)
using namespace std;


int main()
{
    int n;
    cin >> n;

    // 余りの数を格納する配列
    vector<long long> ref(200, 0);

    // 入力の配列
    vector<int> arr(n);

    // 入力配列の数分ループ
    rep(i, n) {
        // 配列の要素を読み込む
        cin >> arr[i];
        // 余りごとの総和をとる
        ref[arr[i] % 200]++;
    }

    // 結果を格納 (long longにしないとWA)
    long long ans = 0;
    // 全余りの可能性を計算
    rep(i, 200) ans += ref[i]*(ref[i]-1)/2;

    cout << ans << endl;
    return 0;
}
