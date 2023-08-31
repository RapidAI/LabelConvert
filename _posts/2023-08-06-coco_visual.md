---
title: Visualize COCO image
author: SWHL
date: 2023-08-31
category: Jekyll
layout: post
---

```bash
coco_visual --vis_num 1 \
            --json_path dataset/YOLOV5_COCO_format/annotations/instances_train2017.json \
            --img_dir dataset/YOLOV5_COCO_format/train2017
```

- `--vis_num`: specify the index of the image to be viewed
- `--json_path`: path to the json file of the image to view
- `--img_dir`: view the directory where the image is located