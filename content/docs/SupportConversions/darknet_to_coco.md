---
weight: 50
date: "2022-09-30"
draft: false
author: "SWHL"
title: "Darknet → COCO"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30"
---


#### 简介
将Darnet格式数据集转化为COCO格式数据集。


#### Darknet结构如下：

{{< alert text="具体结构示例文件，可移步：[darknet_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/darknet_dataset)" />}}

```text {linenos=table}
darknet_dataset
├── class.names
├── gen_config.data
├── gen_train.txt
├── gen_valid.txt
└── images
    ├── train
    └── valid
```

#### 转换
```bash {linenos=table}
darknet_to_coco --data_dir dataset/darknet_dataset
```

- `--data_dir`: COCO格式数据集所在目录。示例为`dataset/darknet_dataset`
- `--save_dir`: 保存转换后的数据集目录。默认为`dataset/darknet_dataset_coco`

#### 转换后结构如下：

{{< alert text="具体结构示例文件，可移步：[COCO_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/COCO_dataset)" />}}

```text {linenos=table}
COCO_dataset
├── annotations
│   ├── instances_train2017.json
│   └── instances_val2017.json
├── train2017
│   ├── 000000000001.jpg
│   └── 000000000002.jpg
└── val2017
    └── 000000000001.jpg
```