---
title: 字符串的编辑距离
author: Tao He
date: 2015-02-17
tag: Algorithm
category: Algorithm
layout: post
---

对于存在差异的字符串，我们可以通过如下三种方式使它们变得相同：

1. 修改一个字符；
2. 增加一个字符；
3. 删除一个字符。

能够通过如上三种变换使得两个字符串相同的最小操作数记为两个字符串的编辑距离。

两个字符串的相似度定义为 **编辑距离+1** 的倒数。

<!--more-->

分析
-----

与最长公共子序列问题类似，可以通过动态规划(Dynamic Programming)的方法来解决这一问题。

状态转移方程如下：

    dis[i][j] = dis[i-1][j-1]; A[i]==B[j]

    dis[i][j] = min(dis[i-1][j-1]+1, dis[i][j-1]+1, dis[i-1][j]+1); A[i]!=B[j]

最终`dis[Alen][Blen]`的值即为所求的编辑距离。

代码实现
---------

~~~cpp
/*
 * 注意：为方便DP，字符串从索引为 1 的位置开始。
 */
int getDistance(char A[], char B[]) {
    int Alen(strlen(A+1)), Blen(strlen(B+1));
    int dis[Alen+5][Blen+5];
    memset(dis, 0, sizeof(dis[0][0])*(Alen+5)*(Blen+5));
    for(int i = 1; i <= Alen; ++i) {
        for(int j = 1; j <= Blen; ++j) {
            if(A[i] == B[j]) {
                dis[i][j] = dis[i-1][j-1];
            }
            else {
                dis[i][j] = min(dis[i-1][j-1]+1,
                        min(dis[i][j-1], dis[i-1][j])+1);
            }
        }
    }
    return dis[Alen][Blen];
}
~~~



