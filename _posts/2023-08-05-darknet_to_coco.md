---
title: darknet → COCO
author: SWHL
date: 2023-08-31
category: Jekyll
layout: post
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
