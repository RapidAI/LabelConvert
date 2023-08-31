---
title: Polya定理及应用
author: Tao He
date: 2015-06-05
tag: Algorithm
category: Algorithm
layout: post
---

概念及定理
-----------

首先是群的概念：

设 $G$ 是一个集合，$\times$ 是 $G$ 上的二元运算，如果 $(G, \times)$ 满足下面的条件：

1. 封闭性：对于任何 $a,b \in G$ 有 $a \times b \in G$；
2. 结合律：对任何 $a,b,c\in G$ 有 $(a \times b) \times c=a \times (b \times c)$；
3. 单位元：存在 $e\in G$，使得对所有的 $a\in G$，都有 $a \times e = e \times a = a$；
4. 逆元：对于每个元素 $a\in G$，存在 $x\in G$，使得 $a \times x = x \times a = e$，这个时候记 $x$ 为 $a^{-1}$，称为 $a$ 的逆元，那么则称 $(G, \times)$ 为一个群。

<!--more-->

例：$G=\{0,1,2,3,4....n-1\}$，那么它在 $\text{mod n}$ 加法下是一个群。

群元素的个数有限，称为有限群，且其中元素的个数称为阶，记为 $\|G\|$，群元素的个数无限，称为无限群。

若对于群元素中的任意两个元素 $a,b$ 都有 $ab=ba$ 那么称 $G$ 为交换群，简称*Abel*群。

置换：设 $X$ 为一个有限集，$\pi$ 是 $X$ 到 $X$ 的一个一一变换，那么称 $\pi$ 是 $X$ 上的一个置换。

例：设 $X=\{1,2,3,4....n\}$，设 $\pi$ 是 $X$ 的一个变换，满足 $\pi: 1\to a_1,2\to a_2,\dots n\to a_n$，其中 $a_1,a_2\dots a_n$ 是 $X$ 的一个
排列，则称 $\pi$ 是 $X$ 上的一个置换。可将 $\pi$ 记为:

$$\begin{array}{|c|c|c|c|c|}\hline
 1 &  2 &  3 &  \dots &  n \\ \hline
 a_1 &  a_2 &  a_3 &  \dots &  a_n \\ \hline
\end{array}$$

同一置换用这样的表示法有 $n!$ 种，但其对应的关系不变。
假设循环 $\pi$ 只这样一个置换，满足 $\pi: a_1\to a_2,a_2\to a_3,\dots a_k\to a_1$，但是对于其他元素保持不变，即：$a\to a$,可将 $\pi$ 记为

$$\begin{array}{|c|c|c|c|c|}\hline
 a_1 &  a_2 &  a_3 &  \dots &  a_k \\ \hline
 a_2 &  a_3 &  a_4 &  \dots &  a_1 \\ \hline
\end{array}$$

称为 $k$ 阶循环，$K$ 为循环长度。每个置换都可以写成若干个互不相交的循环的乘积，且表示是唯一的.如

$$\begin{array}{|c|c|c|c|c|c|} \hline
 1 &  2 &  3 &  4 &  5 &  6 \\ \hline
 2 &  4 &  5 &  1 &  3 &  6 \\ \hline
\end{array}$$

则可以表示为 $(124)(35)(6)$，置换的循环节数是上面的循环个数，上面的例题的循环节数为 $3$。

定义：设 $G$ 是有限集 $X$ 上的置换群，点 $a, b \in X$ 称为"等价"的，当且仅当，存在 $\pi \in G$ 使得 $\pi(a)=b$，记为 $a \sim b$，这种等价条件下，
$X$ 的元素形成的等价类称为 $G$ 的轨道，它是集合 $X$ 的一个子集，$G$ 的任意两个不同的轨道之交是空集，所以置换群 $G$ 的轨道全体是集合 $X$ 的一个划分，
构成若干个等价类，等价类的个数记为 $L$。

+ $Z_k$ ($K$ 不动置换类)：设 $G$ 是 $1 \dots n$ 的置换群。若 $K$ 是 $1 \dots n$ 中某个元素，$G$ 中使 $K$ 保持不变的置换的全体，记以 $Z_k$，叫做 $G$ 中
使 $K$ 保持不动的置换类，简称 $K$ 不动置换类。

+ $E_k$(等价类)：设 $G$ 是 $1 \dots n$ 的置换群。若 $K$ 是 $1 \dots n$ 中某个元素，$K$ 在 $G$ 作用下的轨迹，记作 $E_k$。即 $K$ 在 $G$ 的作用下所能
变化成的所有元素的集合。这个时候有：$|E_k|*|Z_k|=|G|$ 成立 $(k=1,2,.....n)$。

+ $C(\pi)$：对于一个置换 $\pi \in G$，及 $a \in X$，若 $\pi(a)=a$，则称 $a$ 为 $\pi$ 的不动点。$\pi$ 的不动点的全体记为 $C(\pi)$。例如 $\pi=(123)(3)(45)(6)(7), X=\{1,2,3,4,5,6,7\}$；
那么 $C(\pi)=\{3,6,7\}$ 共 $3$ 个元素。

**Burnside引理**：

$$\begin{aligned}
    L &= \frac{1}{\|G\|}*(Z_1+Z_2+Z_3+Z_4+\dots+Z_k) \\
    L &= \frac{L1}{\|G\|}*(C(\pi_1)+C(\pi_2)+C(\pi_3)+\dots+C(\pi_n)), k\in X, \pi \in G
\end{aligned}$$

**Polya定理**：

设 $G=\{\pi_1，\pi_2，\pi_3, \dots, \pi_n\}$ 是 $X=\{a_1，a_2，a_3, \dots, a_n\}$ 上一个置换群，用 $m$ 中颜色对 $X$ 中的元素进行涂色，那么不同的涂色方案
数为：

$$\frac{1}{|G|}*(m^C(\pi_1)+m^C(\pi_2)+m^C(\pi_3)+\dots+m^C(\pi_k))$$

其中 $C(\pi_k)$ 为置换 $\pi_k$ 的循环节的个数。

polya定理求循环节个数
--------------------

~~~cpp
const int MAXN=1001;
int n, perm[MAXN], visit[MAXN]; //sum求循环节个数, Perm用来存储置换,即一个排列
int gcd(int n, int m) {
    return m==0?n:gcd(m,n%m);
}
void Polya() {
    int pos,sum=0;
    memset(visit, 0x00, sizeof(visit));
    for(int i=0; i<n; i++) {
        if(!visit[i]) {
            sum++; pos=i;
            for(int j=0;!visit[perm[pos]];j++) {
                pos=perm[pos];
                visit[pos]=1;
            }
        }
    }
    return sum;
}
~~~

考虑旋转和翻转
-------------

1.旋转置换.

我们假设依次顺时针旋转 $1 \sim n$ 个,则循环个数为 $gcd(i,n)$；

2.翻转置换

+ 当 $n$ 为偶数时，分两种情况：
    + 一种是中心轴在两个对称对象上，则循环个数为 $n/2+1$，这样的置换有 $n/2$ 个。
    + 另一种是对称轴两边分别有 $n/2$ 个对象，则循环个数为 $n/2$，这样的置换也有 $n/2$ 个。

+ 当 $n$ 为奇数时，对称轴就只能在一个对象上，则循环个数为 $n/2+1$。

例题：POJ 2409
--------------

题目链接：[POJ 2409: http://poj.org/problem?id=2409](http://poj.org/problem?id=2409)

> A bracelet is a ring-like sequence of s beads each of which can have one of c distinct colors. The ring is closed, i.e. has no beginning or end, and has no direction. Assume an unlimited supply of beads of each color. For different values of s and c, calculate the number of different bracelets that can be made.

理解：给定颜色种数和环上的珠子总数，问有多少种染色方案（通过旋转和翻转相同的算同一种）。可见，是简单的考虑旋转和翻转的Polya计数模型。题解：

~~~cpp
#include <cstdio>
using namespace std;

inline long long gcd(long long a, long long b) {
    return b==0?a:gcd(b, a%b);
}

long long llpow(long long a, long long b) {
    return b==0?1:llpow(a, b-1)*a;
}

long long polya(long long n, long long m) {
    long long sum = 0;
    for(int i = 1; i <= m; ++i) {
        sum += llpow(n, gcd(m, i));
    }
    if(m & 1) {
        sum += m*llpow(n, (m>>1)+1);
    }
    else {
        sum += (m>>1)*llpow(n, (m>>1)+1) + (m>>1)*llpow(n, m>>1);
    }
    return sum/2/m; // 去掉翻转和旋转的重复
}

int main(int argc, char **argv) {
    long long n, m;
    while(scanf("%lld%lld", &n, &m) != EOF && m+n > 0) {
        printf("%lld\n", polya(n, m));
    }

    return 0;
}
~~~

例题：POJ 2154
---------------

题目链接：[POJ 2154: http://poj.org/problem?id=2154](http://poj.org/problem?id=2154)

题目大意：将正 $n$ 边形的 $n$ 个顶点用 $n$ 种颜色染色，问有多少种方案（答案$\text{mod } p$，且可由旋转互相得到的算一种）。

分析：顺时针旋转 $i$ 格的置换中，循环的个数为 $gcd(i,n)$，每个循环的长度为 $n/gcd(i,n)$。如果枚举旋转的格数 $i$，复杂度显然较高。
因此，考虑不枚举 $i$，反过来枚举 $L$。由于 $L|N$，枚举了 $L$，再计算有多少个 $i$ 使得 $0 \le i \le n-1$ 并且 $L=gcd(i, n)$。即 $gcd(i,n)=n/L$。

不妨设 $a=\frac{n}{L}=gcd(i, n)$，设 $i=a*t$，则当且仅当 $gcd(L,t)=1$ 时，有：
$$Gcd(i,n)=gcd(a*L,a*t)=a$$
因为 $0 \le i < n$，所以 $0 \le t < \frac{n}{a} = L$，所以满足这个条件的 $t$ 的个数为 $Euler(L)$.

欧拉函数：

$$\phi(x)=x(1-\frac{1}{p_1})(1-\frac{1}{p_2})(1-\frac{1}{p_3})\dots(1-\frac{1}{p_k})$$

其中 $p_1, p_2, p_3, \dots, p_k$ 为 $x$ 的所有质因数，$x$ 是不为 $0$ 的整数。**$\phi(n)$ 表示不超过 $n$ 且与 $n$ 互素的正整数的个数**。

~~~cpp
#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

const int maxn = 36000;
int n, mod, ans, prim[35000];
bool flag[maxn + 20];

void get_prim() {
    memset(flag, 0x00, sizeof (flag));
    for(int i = 2; i <= 1000; i++) {
        if(!flag[i]) {
            for(int j = i * i; j <= maxn; j += i) {
                flag[j] = true;
            }
        }
    }
    for(int i = 2, k = 0; i <= maxn; i++) {
        if(!flag[i]) {
            prim[k++] = i;
        }
    }
}

int eular(int n) { // phi function.
    int i = 0, ans = 1;
    for(i = 0; prim[i] * prim[i] <= n; i++) {
        if(n % prim[i] != 0) {
            continue;
        }
        ans *= prim[i] - 1; n /= prim[i];
        while(n % prim[i] == 0) {
            ans *= prim[i]; n /= prim[i];
        }
    }
    if(n > 1) {
        ans *= n - 1;
    }
    return ans % mod;
}

int pow_mod(int c, int k, int mod) {
    int ans = 1;
    c = c % mod;
    while(k) {
        if(k & 1) {
            ans = (c * ans) % mod;
        }
        k >>= 1;
        c = (c * c) % mod;
    }
    return ans;
}

int main() {
    get_prim();
    int i, T;
    scanf("%d", &T);
    while(T-- && scanf("%d%d", &n, &mod)) {
        ans = 0;
        for(i = 1; i * i <= n; i++) {
            if (i * i == n) { //枚举循环长度l，找出相应的i的个数：gcd(i,n)=n/l.
                ans = (ans + pow_mod(n, i - 1, mod) * eular(i)) % mod;
            }
            else if(n % i == 0) { //有长度为l的循环，就会有长度为n/l的循环。
                ans = (ans + pow_mod(n, n / i - 1, mod) * eular(i) +
                        eular(n / i) * pow_mod(n, i - 1, mod)) % mod;
            }
        }
        printf("%d\n", ans);
    }
}
~~~

参考
----

1. [polya 计数法，burnside定理](http://blog.sina.com.cn/s/blog_6f71bea30100opru.html)

