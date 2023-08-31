---
title: Boyer-Moore 算法
author: Tao He
date: 2015-02-14
tag: Algorithm
category: Algorithm
layout: post
---

Boyer-Moore 算法由 Robort S.Boyer 和 J Strother Moore 在1977年提出，可以在O(1)的时间复杂度内完成字符串的匹配，其在绝大部分场合的性能表现要优于KMP算法。
GNU grep使用了此算法进行字符串匹配，同时也被很多文本编辑器用进行字符串的查找。

<!--more-->

移动规则
--------

### “坏字符”规则

坏字符规则(bad-character shift)用来计算当前模式串与源串失配时的模式串指针的移动方案。具体计算方法如下：


    后移位数 = 坏字符的位置 - 坏字符在模式串中的上一次出现位置

式中，坏字符在模式串中的上一次出现位置值可以由一下算法得出：

~~~cpp
/**
 * bmBC数组为对应坏字符的应有的右移距离。
 **/
inline void getBadChar(int bmBC[], int ALPHABET_SIZE, char pattern[]) {
    int len = strlen(pattern);
    for(int i = 0; i < ALPHABET_SIZE; ++i) {
        bmBC[i] = m;
    }
    for(int i = 0; i < len; ++i) {
        bmBC[pattern[i]] = len - 1 - i;
    }
}
~~~

`bmBC`数组基于字典计算，最终计算得到的`bmBC`数组便是每个字母在模式串中出现的最后的位置。

### “好后缀”规则

好后缀规则(good-suffix shift)通过模式串和源字符串的后缀之间的关系来计算模式串指针移动的位置量。具体计算方法如下：

    后移位数 = 好后缀的位置 - 模式串中的上一次出现位置

式中，好后缀的位置的取值以“好后缀”的最后一个字符为准。如果“好后缀”在模式串中没有重复出现，择取其上一次出现的位置为 $-1$。

为了应用好后缀规则，还需要对模式串预处理，求出后缀长度表。即以每一个位置的字符为后缀和以最后一个字符为后缀的公共后缀串的长度。

~~~cpp
/**
 * suffix 数组的含义:
 * suffix[i]为pattern中以i位置字符为后缀和
 * 以pattern中最后一个字符为后缀的公共后缀串的长度。
 */
inline void getSuffix(int suffix[], char pattern[]) {
    int len = strlen(pattern);
    suffix[len-1] = len;
    for(int i = len - 2; i >= 0; --i) {
        int j = i;
        while(j > 0 && pattern[j] == pattern[len-1-(i-j)]) {
            --j;
        }
        suffix[i] = i - j;
    }
}
~~~

通过利用已经求出的后缀串的长度，还可以对该过程做出进一步的改进。如下：

~~~cpp
inline void getSuffix(int suffix[], char pattern[]) {
    int len = strlen(pattern);
    int g = len-1, f;
    suffix[len-1] = len;
    for(int i = len - 2; i >= 0; --i) {
        if(i > g && suffix[(len-1)-(f-i)] < i - g) {
            suffix[i] = suffix[(len-1)-(f-i)];
        }
        else {
            if(i < g) {
                g = i;
            }
            f = i;
            while(g >= 0 && pattern[g] == pattern[(len-1)-(f-g)]) {
                --g;
            }
            suffix[i] = f - g;
        }
    }
}
~~~

通过已经求出的后缀长度表，便可以求出“好后缀”的长度。

~~~cpp
inline void getGoodSuffix(int bmGS[], char pattern[]) {
    int len = strlen(pattern);
    int suffix[len+5];
    getSuffix(suffix, pattern);
    for(int i = 0; i < len; ++i) {
        bmGS[i] = len;
    }
    for(int i = len-1, j = 0; i >= 0; --i) {
        if(suffix[i] == i + 1) {
            for(; j < len - 1 - i; ++j) {
                if(bmGS[j] == len) {
                    bmGS[j] = len - 1 - i;
                }
            }
        }
    }
    for(int i = 0; i <= len-2; ++i) {
        bmGS[len-1-suffix[i]] = len - 1 - i;
    }
}
~~~

算法实现
-------

最终，BoyerMoore算法的实现如下：

~~~cpp
/**
 * 如果模式串存在，返回模式串的第一个字符在文本串中的索引位置（从0开始计算）。
 * 如果不存在，返回 -1 。
 */
int BoyerMoore(char pattern[], char src[]) {
    int ALPHABET_SIZE = 256, len = strlen(pattern);
    int bmBC[ALPHABET_SIZE+5], bmGS[len+5];
    getBadChar(bmBC, ALPHABET_SIZE, pattern);
    getGoodSuffix(bmGS, pattern);
    int j = 0, i;
    while(j <= strlen(src) - len) {
        for(i = len - 1; i >= 0 && pattern[i] == src[i+j]; --i) {
            ;
        }
        if(i < 0) {
            return j;
        }
        else {
            j += max(bmBC[src[i+j]]-(len-1-i), bmGS[i]);
        }
    }

    return -1;
}
~~~

参考
-----

1. [grep之字符串搜索算法Boyer-Moore由浅入深(比KMP快3-5倍)](http://blog.jobbole.com/52830)
2. [字符串匹配的Boyer-Moore算法](http://blog.jobbole.com/39132)



