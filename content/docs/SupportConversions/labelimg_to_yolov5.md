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


- Convert the yolo data format marked by the [labelImg](https://github.com/tzutalin/labelImg) library to YOLOV5 format data with one click.
- The labelImg label data directory structure is as follows (see `dataset/labelImg_dataset` for details):
    ````text
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
- Convert
    ```bash
    labelimg_to_yolov5 --src_dir dataset/labelImg_dataset \
                       --out_dir dataset/labelImg_dataset_output \
                       --val_ratio 0.2 \
                       --have_test true \
                       --test_ratio 0.2
    ```
    - `--src_dir`: the directory where labelImg is stored after labeling.
    - `--out_dir`: the location where the data is stored after conversion.
    - `--val_ratio`: the ratio of the generated validation set to the whole data, default is `0.2`.
    - `--have_test`: whether to generate the test part of the data, the default is `True`.
    - `--test_ratio`: percentage of the whole data of the test data, default is `0.2`.

- Converted directory structure (see `dataset/labelImg_dataset_output` for details):
    ````text
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
- You can further directly convert the `dataset/labelImg_dataset_output` directory to COCO
    ```bash
    yolov5_to_coco --data_dir dataset/labellImg_dataset_output
    ````
