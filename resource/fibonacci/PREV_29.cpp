#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;
typedef long long LL;
const int N = 2;
LL MOD;

struct Matrix {
    LL m[N][N];
};

Matrix I = {1,0,0,1};
Matrix A = {1,1,1,0};

LL multiply(LL a,LL b) {
    LL ans = 0;
    a %= MOD;

    while (b) {
        if (b & 1) {
            ans = (ans + a) % MOD;
            b--;
        }

        b >>= 1;
        a = (a + a) % MOD;
    }

    return ans;
}

Matrix multi(Matrix a,Matrix b) {
    Matrix c;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            c.m[i][j] = 0;

            for (int k=0; k<N; k++) {
                c.m[i][j] = (c.m[i][j] % MOD + multiply(a.m[i][k] % MOD,b.m[k][j] % MOD)) % MOD;
                c.m[i][j] %= MOD;
            }
        }
    }

    return c;
}

Matrix power(LL n) {
    Matrix ans = I,p = A;

    while (n) {
        if (n & 1) {
            ans = multi(ans,p);
            n--;
        }

        n >>= 1;
        p = multi(p,p);
    }

    return ans;
}

LL Work(LL n,LL m) {
    LL k = n % m;
    Matrix ans = power(m-k-1);

    if (k & 1) {
        return ans.m[0][0];
    }
    else {
        Matrix ans1 = power(m-1);
        LL tmp = ans1.m[0][0] - ans.m[0][0];
        tmp = (tmp % MOD + MOD) % MOD;
        return tmp;
    }
}

LL Solve(LL n,LL m) {
    LL t = n / m;
    LL k = n % m;
    LL r = t / 2;
    Matrix ans = I;

    if (m & 1) {
        if (t % 2 == 0 && r % 2 == 0) {
            if (k == 0) {
                return 0;
            }

            ans = power(k-1);
            LL ret = ans.m[0][0];
            ret = (ret % MOD + MOD - 1) % MOD;
            return ret;
        }

        if (t % 2 == 0 && r % 2 == 1) {
            LL ret = 0;

            if (k) {
                ans = power(k-1);
                ret = ans.m[0][0];
                Matrix ans1 = power(m-1);
                ret = ans1.m[0][0] - ret;
                ret = (ret % MOD + MOD - 1) % MOD;
                return ret;
            }
        }

        if (t % 2 == 1 && r % 2 == 0) {
            LL ret = Work(n,m);
            ret--;
            ret = (ret % MOD + MOD) % MOD;
            return ret;
        }

        if (t % 2 == 1 && r % 2 == 1) {
            LL ret = Work(n,m);
            Matrix ans1 = power(m-1);
            ret = ans1.m[0][0] - 1 - ret;
            ret = (ret % MOD + MOD) % MOD;
            return ret;
        }
    }
    else {
        if (t & 1) {
            LL ret = Work(n,m);
            ret--;
            ret = (ret % MOD + MOD) % MOD;
            return ret;
        }
        else {
            if (k == 0) {
                return 0;
            }

            ans = power(k-1);
            LL ret = ans.m[0][0];
            ret = (ret % MOD + MOD - 1) % MOD;
            return ret;
        }
    }
}

int main() {
    LL n,m;

    while (cin>>n>>m>>MOD) {
        n += 2;

        if (n == m) {
            Matrix ans = power(m-1);
            LL ret = ans.m[0][0] - 1;
            ret = (ret % MOD + MOD) % MOD;
            cout<<ret<<endl;
            continue;
        }

        cout<<Solve(n,m)<<endl;
    }

    return 0;
}
