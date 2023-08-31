---
title: 星期的计算
author: Tao He
date: 2015-02-16
tag: Algorithm
category: Algorithm
layout: post
---

经常需要通过日期来计算对应的星期，相关的方法主要有蔡勒公式和基姆拉尔森公式。

蔡勒公式
---------

### 蔡勒(Zeller)公式

$$w = (y+\lfloor{y/4}\rfloor+\lfloor{c/4}\rfloor-2c+\lfloor{26(m+1)/10}\rfloor+d-1) \textit{ mod } 7$$

### 参数含义解释

蔡勒公式中个参数的含义如下：

+ $y$: 年份的后两位数；
+ $c$: 年份的前两位数；
+ $m$: 月份；**注意**：月份的值在3-14之间，1月和2月应当作为上一年的13、14月来考虑。
+ $d$: 日。

<!--more-->

### 使用范围

蔡勒公式只适用于格里高利历（现在时间通用的公历），即**1582年10月15日**之后的情形。

### 代码实现(Python)

~~~python
def getWeek(year, mouth, day):
    ''' Zeller Method.
    '''
    if mouth < 3:
        year, mouth = year-1, mouth+12
    y, c = int(str(year)[2:4]), int(str(year)[0:2])
    week = (y + y//4 + c//4 - 2*c + 26*(mouth+1)//10 + day - 1) % 7
    return week
~~~

基姆拉尔森公式
----------------

### 基姆拉尔森公式

$$ w = (y/400-y/100+y/4+y+3*(m+1)/5+2*m+d+1) \textit{ mod } 7 $$

### 参数含义解释

公式中个参数的含义如下：

+ $y$: 年份的后两位数；
+ $c$: 年份的前两位数；
+ $m$: 月份；**注意**：月份的值在3-14之间，1月和2月应当作为上一年的13、14月来考虑。
+ $d$: 日。




