---
weight: 20
date: "2022-09-30T05:33:22+01:00"
draft: false
author: "SWHL"
title: "COCO → labelImg yolo"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30T05:33:22+01:00"
---

- One-click conversion of COCO format data to labelImg labeled yolo format data.
- COCO format directory structure（see `dataset/COCO_format` for details）：
    ```text {linenos=table}
    COCO_format
    ├── annotations
    │   ├── instances_train2017.json
    │   └── instances_val2017.json
    ├── train2017
    │   ├── 000000000001.jpg
    │   └── 000000000002.jpg
    └── val2017
        └── 000000000001.jpg
    ```
- Convert
    ```bash {linenos=table}
    coco_to_labelImg --data_dir dataset/COCO_format
    ```
  - `--data_dir`: the directory where the COCO format dataset is located. Default is `dataset/COCO_format`.
- Converted directory structure (see `dataset/labelImg_format` for details):
  ```text {linenos=table}
  labelImg_format
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
- For the converted directory, you can directly use the [labelImg](https://github.com/tzutalin/labelImg)  library to open it directly and change the label. The specific commands are as follows:
  ```bash {linenos=table}
  $ cd dataset/labelImg_format
  $ labelImg train train/classes.txt

  # or
  $ labelImg val val/classes.txt
  ```
