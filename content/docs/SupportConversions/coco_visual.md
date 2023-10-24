---
weight: 60
date: "2022-09-30T05:33:22+01:00"
draft: false
author: "SWHL"
title: "Visualize COCO image"
icon: "bike_scooter"
toc: true
description: ""
publishdate: "2022-09-30T05:33:22+01:00"
---


```bash {linenos=table}
coco_visual --vis_num 1 \
            --json_path dataset/COCO_format/annotations/instances_train2017.json \
            --img_dir dataset/COCO_format/train2017
```

- `--vis_num`: specify the index of the image to be viewed
- `--json_path`: path to the json file of the image to view
- `--img_dir`: view the directory where the image is located