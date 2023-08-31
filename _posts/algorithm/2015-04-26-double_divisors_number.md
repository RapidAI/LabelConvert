---
title: 约数个数加倍
author: Tao He
date: 2015-04-26
tag: Algorithm
category: Algorithm
layout: post
---

最近在[Project Euler](https://projecteuler.net)上看到一道很有意思的题目，题目大意是找到一个最小的正整数，这个正整数有 $2^{500500}$ 个约数。将原题摘引如下：

> The number of divisors of 120 is 16.

> In fact 120 is the smallest number having 16 divisors.

> Find the smallest number with 2<sup>500500</sup> divisors.

> Give your answer modulo 500500507.

<!--more-->

题目链接：[Problem 500. Problem 500!!!](https://projecteuler.net/problem=500 "Problem 500")

第一眼看到这个题目，毫无头绪。一番Google之后，找到了如下一个题解：

引自[https://news.ycombinator.com/item?id=8977550](https://news.ycombinator.com/item?id=8977550)的关于此题的解答：

> So at this point, we think about doubling factor count and the ways we can do it. Out options are:
>   <1>. Multiply by a prime that we have never used so far.
>   <2>. Multiply by an existing prime k + 1 times, where k is the number of times it has been used.
> We repeat this 500500 times, using rule <1> and <2> (which can be generalized to one rule) and the result is the final answer.

| factor count | n                         |
|:------------:|---------------------------|
|  2           | 2                         |
|  4           | 2*3 <1>                   |
|  8           | 2*3*2*2 <2>               |
|  16          | 2*3*2*2*5 <1>             |
|  32          | 2*3*2*2*5*7 <1>           |
|  64          | 2*3*2*2*5*7*3*3 <2>       |
|  128         | 2*3*2*2*5*7*3*3*11 <1>    |

> For 16 factors the number works out to be 120 (just like the example!). For numbers shown in the questions, sieving the prime takes some time, I also found it helpful to use a binary heap for speeding up finding the next smallest factors.

这个解法的核心在于使约数个数加倍的规则。借助[WolframAlpha](http://www.wolframalpha.com/)，我们求得第500500个质数的值为7376507。因此，只需要先将前500500个质数（这个值可以更少一点）压入优先队列，每次按照上面讲到的规则出队、入队、在O(n)的时间内求得结果。我们知道，初始化质数表的时间复杂度，而筛法的时间复杂度是O(n(lg(lgn)))的(埃拉托斯特尼筛法(sieve of Eratosthenes))。在这个过程中需要维护一个堆，复杂度为O(n(lg n))。因此，这个题目的时间复杂度为O(n(lg n))。

从这个题的求解来看，真心可以体会到**算法和数据结构改变世界**!

下面给出这一算法的Python实现。

~~~python
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from heapq import heappush, heappop

class comb:
    def __init__(self, n, c, nc):
        self.n = n
        self.c = c
        self.nc = nc
    def __cmp__(self, other):
        return self.nc - other.nc
    def __lt__(self, other):
        return self.nc < other.nc
    def __gt__(self, other):
        return self.nc > other.nc
    def __eq__(self, other):
        return self.nc == other.nc
    def __str__(self):
        return '(%d,%d,%d)'%(self.n, self.c, self.nc)

def nextprime():
    n, bound = 5, 7376507  # bound is the 500500th prime.
    yield 2
    yield 3
    while n < bound:
        i, r = 2, int(sqrt(n))
        while i <= r:
            if n % i == 0:
                break
            i += 1
        if i > r:
            yield n
        n += 1

def solve500():
    n, mod, bound, mult, p = 1, 500500507, 500500, 1, 0
    heap, prime = [], nextprime()

    for i in range(1, 500500):
        p = next(prime)
        heappush(heap, comb(p, 1, p))

    while n <= bound:
        h, n = heappop(heap), n+1
        mult = (mult*h.nc) % mod
        heappush(heap, comb(h.n, 2*h.c, h.nc*h.nc))

    return mult

if __name__ == '__main__':
    print(solve500())

# vim: set sw=4, ts=4
~~~

答案(answer): 35407281

此外，在网站[oeis.org/wiki](http://oeis.org/wiki/Number_of_divisors_function#Formulae_for_the_number_of_divisors_function)上还有其他的一些关于如何计算一个数的约数个数的公式和资料。

