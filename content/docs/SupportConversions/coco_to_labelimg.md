---
weight: 20
date: "2022-09-30"
draft: false
author: "SWHL"
title: "COCO → labelImg yolo"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30"
---

#### 简介
将COCO格式数据集转换为可以直接用[labelImg](https://github.com/HumanSignal/labelImg)工具可视化标注的YOLO格式。


#### COCO结构如下：

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

#### 转换
```bash {linenos=table}
coco_to_labelImg --data_dir dataset/COCO_dataset --save_dir dataset/labelImg_format
```

- `--data_dir`: COCO格式数据集所在目录。示例为`dataset/COCO_dataset`
- `--save_dir`: 保存转换后的数据集目录。默认为`dataset/COCO_dataset_labelImg`

#### 转换后结构如下：

{{< alert text="具体结构示例文件，可移步：[labelImg_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/labelImg_dataset)" />}}


```text {linenos=table}
labelImg_dataset
  ├── train
  │   ├── 000000000001.jpg
  │   ├── 000000000001.txt
  │   ├── 000000000002.jpg
  │   └── classes.txt
  └── val
      ├── 000000000001.jpg
      ├── 000000000001.txt
      └── classes.txt
```

#### labelImg可视化
```bash {linenos=table}
$ cd dataset/labelImg_dataset
$ labelImg train train/classes.txt

# or
$ labelImg val val/classes.txt
```
