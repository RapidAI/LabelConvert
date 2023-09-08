---
weight: 53
date: "2022-09-30T05:33:22+01:00"
draft: false
author: "SWHL"
title: "YOLOV5 YAML → COCO"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30T05:33:22+01:00"
tags: ["Beginners"]
categories: [""]

twitter:
  card: "summary"
  site: "@LotusDocs"
  creator: "@LotusDocs"
  title: "What is Lotus Docs?"
  description: "Overview of Lotus Docs"
  image: ""
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