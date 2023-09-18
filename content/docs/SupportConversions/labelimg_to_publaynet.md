---
weight: 11
date: "2022-09-30T05:33:22+01:00"
draft: false
author: "SWHL"
title: "labelImg → PubLayNet"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30T05:33:22+01:00"
---


- Convert the yolo data format marked by the [labelImg](https://github.com/tzutalin/labelImg) library to PubLayNet format data with one click.
- The labelImg label data directory structure is as follows (see `dataset/labelImg_dataset` for details):
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
- Convert
    ```bash {linenos=table}
    labelImg_to_publaynet --data_dir dataset/labelImg_dataset \
                          --val_ratio 0.2 \
                          --have_test true \
                          --test_ratio 0.2
    ```
    - `--data_dir`: the directory where labelImg is stored after labeling.
    - `--val_ratio`: the ratio of the generated validation set to the whole data, default is `0.2`.
    - `--have_test`: whether to generate the test part of the data, the default is `True`.
    - `--test_ratio`: percentage of the whole data of the test data, default is `0.2`.

- Converted directory structure (see `dataset/labelImg_dataset_publaynet` for details):
    ````text {linenos=table}
    labelImg_dataset_publaynet
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
