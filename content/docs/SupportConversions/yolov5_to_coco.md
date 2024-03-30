---
weight: 30
date: "2022-09-30T"
draft: false
author: "SWHL"
title: "YOLOV5 → COCO"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30T"
---

#### 简介
将YOLOv5格式数据集转换为COCO格式。

支持标注格式为矩形框和多边形框。

#### YOLOV5数据结构如下

{{< alert text="具体结构示例文件，可移步：[yolov5_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/yolov5_dataset)" />}}


```text {linenos=table}
yolov5_dataset
├── classes.txt
├── non_labels  # 通常用来放负样本
│   └── bg1.jpeg
├── images
│   ├── images(13).jpg
│   └── images(3).jpg
├── labels
│   ├── images(13).txt
│   └── images(3).txt
├── train.txt
└── val.txt
```

#### 转换
```bash {linenos=table}
yolov5_to_coco --data_dir dataset/yolov5_dataset --mode_list train,val
```

- `--data_dir`: 数据集所在目录。示例为`dataset/yolov5_dataset`
- `--save_dir`: 保存转换后的数据集目录。默认为`dataset/yolov5_dataset_coco`
- `--mode_list`: 指定划分的数据集种类。 (例如：`train,val,test` / `train,val`)

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
