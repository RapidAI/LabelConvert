---
weight: 35
date: "2023-10-31"
draft: false
author: "SWHL"
title: "labelme → COCO"
icon: "circle"
toc: true
description: ""
publishdate: "2023-10-31"
---


#### 简介
一键转换[labelme](https://github.com/wkentaro/labelme)标注的数据格式为COCO格式

#### labelme结构如下：

{{< alert text="具体结构示例文件，可移步：[labelme_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/labelme_dataset)" />}}

```text {linenos=table}
labelme_dataset
├── val_0001.jpg
├── val_0001.json
├── val_0002.jpg
└── val_0002.json
```

#### 转换
```bash {linenos=table}
labelme_to_coco --src_dir dataset/labelme_dataset \
                --out_dir dataset/coco_dataset \
                --val_ratio 0.2 \
                --have_test \
                --test_ratio 0.2
```
- `--src_dir`: labelme标注的数据所在路径
- `--out_dir`: 转换后数据存储路径
- `--val_ratio`: 验证集所占比例，默认是总量的0.2
- `--have_test`: 是否划出测试集，默认是False，如果想要划分测试集，直接加上该参数即可。
- `--test_ratio`: 测试集的比例，默认是总量的0.2

#### 转换后结构如下：

{{< alert text="具体结构示例文件，可移步：[COCO_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/COCO_dataset)" />}}


```text
COCO_dataset
├── annotations
│   ├── instances_train2017.json
│   └── instances_val2017.json
├── train2017
│   ├── 000000000001.jpg
│   └── 000000000002.jpg
└── val2017
    └── 000000000002.jpg
```