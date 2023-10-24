---
weight: 30
date: "2022-09-30T05:33:22+01:00"
draft: false
author: "SWHL"
title: "YOLOV5 → COCO"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30T05:33:22+01:00"
---

- Some background images can be added to the training by directly placing them into the `backgroud_images` directory.
- The conversion program will automatically scan this directory and add it to the training set, allowing seamless integration with subsequent [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) training.
- YOLOV5 training format directory structure (see `dataset/YOLOV5` for details).
    ```text {linenos=table}
    YOLOV5
    ├── classes.txt
    ├── background_images  # usually images that are easily confused with the object to be detected
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
- The image paths in train.txt and val.txt can be either:
  - Path relative to **root directory**:
    ```text {linenos=table}
    dataset/YOLOV5/images/images(3).jpg
    ```
  - Path relative to **dataset/YOLOV5**:
    ```text {linenos=table}
    images/images(3).jpg
    ```
- Convert
    ```bash {linenos=table}
    yolov5_to_coco --data_dir dataset/YOLOV5 --mode_list train,val
    ```
  - `--data_dir`: the directory where the collated dataset is located
  - `--mode_list`: specify the generated json, provided that there is a corresponding txt file, which can be specified separately. (e.g. `train,val,test`)

- The structure of the converted directory (see `dataset/COCO_format` for details)
    ```text {linenos=table}
    COCO_format
    ├── annotations
    │   ├── instances_train2017.json
    │   └── instances_val2017.json
    ├── train2017
    │   ├── 000000000001.jpg
    │   └── 000000000002.jpg  # This is the background image.
    └── val2017
        └── 000000000001.jpg
    ```
