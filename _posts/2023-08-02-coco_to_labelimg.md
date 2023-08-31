---
title: COCO → labelImg yolo
author: SWHL
date: 2023-08-31
category: Jekyll
layout: post
---

- One-click conversion of COCO format data to labelImg labeled yolo format data.
- COCO format directory structure（see `dataset/YOLOV5_COCO_format` for details）：
    ```text
    YOLOV5_COCO_format
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
    ```bash
    coco_to_labelimg --data_dir dataset/YOLOV5_COCO_format
    ```
  - `--data_dir`: the directory where the COCO format dataset is located. Default is `dataset/YOLOV5_COCO_format`.
- Converted directory structure (see `dataset/COCO_labelImg_format` for details):
  ```text
  COCO_labelImg_format
    ├── train
    │   ├── 000000000001.jpg
    │   ├── 000000000001.txt
    │   |-- 000000000002.jpg
    │   └── classes.txt
    └── val
        ├── 000000000001.jpg
        ├── 000000000001.txt
        └── classes.txt
  ```
- For the converted directory, you can directly use the [labelImg](https://github.com/tzutalin/labelImg)  library to open it directly and change the label. The specific commands are as follows:
  ```bash
  $ cd dataset/COCO_labelImg_format
  $ labelImg train train/classes.txt

  # or
  $ labelImg val val/classes.txt
  ```