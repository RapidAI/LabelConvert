---
weight: 55
date: "2022-09-30T05:33:22+01:00"
draft: false
author: "SWHL"
title: "darknet → COCO"
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

- Darknet training data directory structure (see `dataset/darknet` for details).
    ```text
    darknet
    ├── class.names
    ├── gen_config.data
    ├── gen_train.txt
    ├── gen_valid.txt
    └── images
        ├── train
        └── valid
    ```
- Convert
    ```bash
    darknet_to_coco --data_path dataset/darknet/gen_config.data
    ```
