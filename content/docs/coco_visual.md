---
weight: 56
date: "2022-09-30T05:33:22+01:00"
draft: false
author: "SWHL"
title: "Visualize COCO image"
icon: "circle"
toc: true
description: "Lotus Docs is a modern documentation theme built for Hugo."
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


```bash
coco_visual --vis_num 1 \
            --json_path dataset/YOLOV5_COCO_format/annotations/instances_train2017.json \
            --img_dir dataset/YOLOV5_COCO_format/train2017
```

- `--vis_num`: specify the index of the image to be viewed
- `--json_path`: path to the json file of the image to view
- `--img_dir`: view the directory where the image is located