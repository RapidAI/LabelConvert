---
weight: 10
date: "2022-09-30T05:33:22+01:00"
draft: false
author: "SWHL"
title: "labelImg → YOLOV5"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30T05:33:22+01:00"
---

#### 简介
一键将[labelImg](https://github.com/tzutalin/labelImg)标注的数据格式转为YOLO格式

#### labelImg目录格式
详情参见：[`dataset/labelImg_dataset`](https://github.com/RapidAI/LabelConvert/tree/d364199d87e13dd8267efc41cb4a5ea2bb0a370c/dataset/labelImg_dataset)
````text {linenos=table}
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
````

#### 转换
```bash {linenos=table}
labelImg_to_yolov5 --src_dir dataset/labelImg_dataset \
                    --out_dir dataset/labelImg_dataset_output \
                    --val_ratio 0.2 \
                    --have_test \
                    --test_ratio 0.2
```
- `--src_dir`: labelme标注的数据所在路径
- `--out_dir`: 转换后数据存储路径
- `--val_ratio`: 验证集所占比例，默认是总量的0.2
- `--have_test`: 是否划出测试集，默认是False，如果想要划分测试集，直接加上该参数即可。
- `--test_ratio`: 测试集的比例，默认是总量的0.2

#### 转换后目录结构
详情参见：[`dataset/labelImg_dataset_output`](https://github.com/RapidAI/LabelConvert/tree/d364199d87e13dd8267efc41cb4a5ea2bb0a370c/dataset/labelImg_dataset_output)

````text {linenos=table}
labelImg_dataset_output/
├── classes.txt
├── images
│   ├── images(13).jpg
│   ├── images(3).jpg
│   ├── images4.jpg
│   ├── images5.jpg
│   └── images7.jpg
├── labels
│   ├── images(13).txt
│   ├── images(3).txt
│   ├── images4.txt
│   ├── images5.txt
│   └── images7.txt
├── non_labels        # This is the catalog without the labeled images.
│   └── images6.jpg
├── test.txt
├── train.txt
└── val.txt
````

#### 进一步转换为COCO格式
```bash {linenos=table}
yolov5_to_coco --data_dir dataset/labellImg_dataset_output
````
