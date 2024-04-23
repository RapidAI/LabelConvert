---
weight: 60
date: "2022-09-30T"
draft: false
author: "SWHL"
title: "可视化COCO数据集"
icon: "bike_scooter"
toc: true
description: ""
publishdate: "2022-09-30"
---


#### 可视化
```bash {linenos=table}
vis_coco --img_id 1 --json_path dataset/COCO_format/annotations/instances_train2017.json -img_dir dataset/COCO_format/train2017
```

- `--img_id`: 指定显示图像的索引值，示例为1
- `--json_path`: 图像所在的json路径
- `--img_dir`: 图像所在的目录


#### JSON格式示例
```json {linenos=table}
{
    "info": {
      "year": 2022,
      "version": "1.0",
      "description": "For object detection",
      "date_created": "2022"
    },
    "licenses":  [{
        "id": 1,
        "name": "Apache License v2.0",
        "url": "https://github.com/RapidAI/YOLO2COCO/LICENSE"
    }],
    "images": [{
        "date_captured": "2022",
        "file_name": "000000000001.jpg",
        "id": 1,
        "height": 224,
        "width": 224
    }, {
        "date_captured": "2022",
        "file_name": "000000000002.jpg",
        "id": 2,
        "height": 424,
        "width": 550
    }],
    "annotations": [{
        "segmentation": [[18.00, 2.99, 105.00, 2.99, 105.00, 89.00, 18.00, 89.00]],
        "area": 7482.011,
        "iscrowd": 0,
        "image_id": 1,  // Corresponding to the ID in images
        "bbox": [18.00, 2.99, 87.00, 86.00],  // [x, y, w, h], (x,y) is the left top point of the box. w,h is the width and height of the box.
        "category_id": 1,  // Corresponding to the ID in categories.
        "id": 1  // Number that uniquely distinguishes different dimension instances
    }, {
        "segmentation": [
            [126.99, 3.99, 210.99, 3.99, 210.99, 88.99, 126.99, 88.99]
        ],
        "area": 7139.994,
        "iscrowd": 0,
        "image_id": 1,
        "bbox": [126.99, 3.99, 84.0, 84.99],
        "category_id": 1,
        "id": 2
    }],
    "categories": [{
        "supercategory": "stamp",
        "id": 1,
        "name": "stamp"
    }]
}
```

#### 相关信息
- [MSCOCO数据标注详解](https://blog.csdn.net/wc781708249/article/details/79603522)