---
weight: 11
date: "2022-09-30"
draft: false
author: "SWHL"
title: "labelImg → PubLayNet"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30"
---

#### 简介
将labelImg格式数据集转换为PubLayNet格式。


#### labelImg结构如下：

{{< alert text="具体结构示例文件，可移步：[labelImg_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/labelImg_dataset)" />}}

```text {linenos=table}
labelImg_dataset
├── classes.txt
├── images(13).jpg
├── images(13).txt
├── images(3).jpg
├── images(3).txt
├── images4.jpg
├── images4.txt
├── images5.jpg
├── images5.txt
├── images6.jpg
├── images7.jpg
└── images7.txt
```

#### 转换

```bash {linenos=table}
labelImg_to_publaynet --data_dir dataset/labelImg_dataset \
                       --val_ratio 0.2 \
                       --have_test \
                       --test_ratio 0.2
```


- `--data_dir`: COCO格式数据集所在目录。示例为`dataset/labelImg_dataset`
- `--save_dir`: 保存转换后的数据集目录。默认为`dataset/labelImg_dataset_publaynet`
- `--val_ratio`: 验证集数目占数据集总数比例，默认为`0.2`.
- `--have_test`: 是否有测试集。默认为`False`，如果出现，则为`True`
- `--test_ratio`: 测试集数目占数据集总数比例，默认为`0.2`


#### 转换后结构如下：

{{< alert text="具体结构示例文件，可移步：[publaynet_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/publaynet_dataset)" />}}


````text {linenos=table}
publaynet_dataset
├── test
│   ├── images5.jpg
│   └── images5.txt
├── test.json
├── train
│   ├── images(13).jpg
│   ├── images(13).txt
│   ├── images(3).jpg
│   ├── images(3).txt
│   ├── images4.jpg
│   ├── images4.txt
│   ├── images5.jpg
│   ├── images5.txt
│   ├── images7.jpg
│   └── images7.txt
├── train.json
├── val
│   ├── images(13).jpg
│   ├── images(13).txt
│   ├── images5.jpg
│   ├── images5.txt
│   ├── images7.jpg
│   └── images7.txt
└── val.json
````
