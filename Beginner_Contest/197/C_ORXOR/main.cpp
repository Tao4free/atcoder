#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < n; ++i)
using namespace std;


int main()
{
    int n; 
    cin >> n;
    vector<int> a(n);
    rep(i, n) cin >> a[i];


    int ans = 1 << 30;
    rep(s, 1 << (n-1)) {
        int now = 0;
        int o = 0;
        rep(i,n) {
            o |= a[i];
            if (s >> i & 1) {
                now ^= o;
                o =0;
            }
        }

        now ^= o;
        ans = min(ans, now);
    }
    cout << ans << endl;
    return 0;
}
