---
title: Sleep Sort
author: Tao He
date: 2015-02-08
tag: Algorithm
category: Algorithm
layout: post
---

Sleep Sort 是一种通过多线程的不同休眠时间的排序方法。可以很简单地用Shell脚本实现。

~~~bash
#! /bin/bash

function func() {
    sleep "$1"
    echo "$1"
}

while [ -n "$1" ]
do
    func "$1" &
    shift
done
wait
~~~

<!--more-->

很显然，其时间复杂度与排序的数据有关（在绝大多数场合下，并不是一种实用的排序算法）。



