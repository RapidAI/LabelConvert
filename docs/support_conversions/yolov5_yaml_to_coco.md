---
comments: true
---

#### 简介

将以 yaml 文件给出的 YOLOv5 格式数据集转换为 COCO 格式

支持标注格式为矩形框和多边形框。

#### YOLOv5 yaml 结构如下

!!! tip

    具体结构示例文件，可移步：[yolov5_yaml_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/yolov5_yaml_dataset)

```text linenums="1"
yolov5_yaml_dataset
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

#### 转换

```bash linenums="1"
yolov5_yaml_to_coco --yaml_path dataset/yolov5_yaml_dataset/sample.yaml
```

- `--yaml_path`: yaml 文件路径
- `--save_dir`: 保存转换后的数据集目录。默认为 `dataset/yolov5_yaml_dataset_coco`

#### 转换后结构如下

!!! tip

    具体结构示例文件，可移步：[COCO_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/COCO_dataset)

```text linenums="1"
COCO_dataset
├── annotations
│   ├── instances_train2017.json
│   └── instances_val2017.json
├── train2017
│   ├── 000000000001.jpg
│   └── 000000000002.jpg
└── val2017
    └── 000000000001.jpg
```
