---
title: YOLOV5 YAML → COCO
author: SWHL
date: 2023-08-31
category: Jekyll
layout: post
---

- The YOLOV5 yaml data file needs to contain.
    ```text
    YOLOV5_yaml
    ├── images
    │   ├── train
    │   │   ├── images(13).jpg
    │   │   └── images(3).jpg
    │   └── val
    │       ├── images(13).jpg
    │       └── images(3).jpg
    ├── labels
    │   ├── train
    │   │   ├── images(13).txt
    │   │   └── images(3).txt
    │   └── val
    │       ├── images(13).txt
    │       └── images(3).txt
    └── sample.yaml
    ```

- Convert
    ```bash
    yolov5_yaml_to_coco --yaml_path dataset/YOLOV5_yaml/sample.yaml
    ```