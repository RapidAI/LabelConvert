---
title: 树的最长路径
author: Tao He
date: 2015-02-01
tag: Algorithm
category: Algorithm
layout: post
---

树的最长路问题是一类求解树上两点之间最长距离的问题。针对此问题，有这样两类算法：DFS求解和树形DP。本文将以 [HihoCoder 1050 : 树中的最长路](http://hihocoder.com/problemset/problem/1050) 一题为例，
详细阐述这两种解法。

<!--more-->

## 树形DP

树形DP的基本思路为由子节点的情况推出父节点的情况，针对树的最长路径这一问题，分别记录每个节点的子节点的最大深度和次大深度，父节点的最大深度等于所有子节点
的最大深度和次大深度的最大值加1，父节点的次大深度等于所有子节点的最大深度和次大深度的次大值加1，最后，每个节点对应的最长路径值为该节点的 `最大深度-次大深
度+1`, 由此可得到树的最长路径长度。伪代码描述如下：

~~~cpp
初始值：
    depth_0[leaf node] = depth_1[leaf node] = 1
递推：
    depth_0[parent] = max({depth_0[{sons}], depth_1[{sons}]})
    depth_1[parent] = max({depth_0[{sons}], depth_1[{sons}]} - depth_0[parent])
求解：
    length[i] = depth_0[i] + depth_1[i] - 1
    longest = max({length[i]})
~~~

由此，得到结果。

## BFS求解

此题通过BFS求解的算法正确性基于以下性质：

以树上的任意一点为根节点，距离根节点最远的点一定是树的最长路径的一个端点。

证明：假设 $s-t$ 这条路径为树的最长路径，分以下两种情况证明：

1. 设 $u$ 为 $s-t$ 路径上的一点，结论显然成立，否则设搜到的最远点为 $T$ 则 $dis(u,T) > dis(u,s)$ 且 $dis(u,T) > dis(u,t)$，则最长路不是 $s-t$ 了，
与假设矛盾。
2. 设 $u$ 不为 $s-t$ 路径上的点，首先明确，假如 $u$ 走到了 $s-t$ 路径上的一点，那么接下来的路径肯定都在 $s-t$ 上了，而且终点为 $s$ 或 $t$，在1中已经
证明过了。

所以现在又有两种情况了：

1. $u$ 走到了 $s-t$ 路径上的某点，假设为 $X$，最后肯定走到某个端点，假设是 $t$ ，则路径总长度为 $dis(u,X)+dis(X,t)$。
2. $u$ 走到最远点的路径 $u-T$ 与 $s-t$ 无交点，则 $dis(u-T) > dis(u,X)+dis(X,t)$。显然，如果这个式子成立，则
$$dis(u,T)+dis(s,X)+dis(u,X) > dis(s,X)+dis(X,t) = dis(s,t)$$
与最长路不是 $s-t$ 矛盾。

由此上性质，得到如下解法：从任意一点对树BFS，找出深度最大的点，该点即为树的最长路径的一个端点。再从该点出发，对树进行一次BFS，此时得到的深度最大的点，
该点即为树的最长路径的另一个端点，此时改点的深度值即为树的最长路径的长度。

## 代码实现

[HihoCoder 1050](http://hihocoder.com/problemset/problem/1050)

~~~cpp
#include <cstdio>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;

vector<int> e[100100];
bool flag[100100];
int depth[100100], ans, n;

int bfs(int start) {
    memset(flag, 0x00, sizeof(flag));
    memset(depth, 0x00, sizeof(depth));
    queue<int> Q;
    Q.push(start);
    flag[start] = true;
    while(!Q.empty()) {
        int u = Q.front();
        Q.pop();
        for(int i = 0; i < e[u].size(); ++i) {
            if(!flag[e[u][i]]) {
                depth[e[u][i]] = depth[u]+1;
                flag[e[u][i]] = true;
                Q.push(e[u][i]);
            }
        }
    }
    int point = -1;
    ans = -1;
    for(int i = 1; i <= n; ++i) {
        if(depth[i] > ans) {
            ans = depth[i];
            point = i;
        }
    }
    return point; // 返回距离最远的点的编号
}

int main(int argc, char **argv) {
    int x, y;
    scanf("%d", &n);
    for(int i = 1; i < n; ++i) {
        scanf("%d %d", &x, &y);
        e[x].push_back(y);
        e[y].push_back(x);
    }
    bfs(bfs(1));
    printf("%d", ans);

    return 0;
}
~~~

