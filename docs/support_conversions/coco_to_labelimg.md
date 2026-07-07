---
comments: true
---

#### 简介

将 COCO 格式数据集转换为可以直接用 [labelImg](https://github.com/HumanSignal/labelImg) 工具可视化标注的 YOLO 格式。

#### COCO 结构如下

!!! tip

    具体结构示例文件，可移步：[COCO_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/COCO_dataset)

```text linenums="1" linenums="1"
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

#### 转换

```bash linenums="1"
coco_to_labelImg --data_dir dataset/COCO_dataset --save_dir dataset/labelImg_format
```

- `--data_dir`: COCO 格式数据集所在目录。示例为 `dataset/COCO_dataset`
- `--save_dir`: 保存转换后的数据集目录。默认为 `dataset/COCO_dataset_labelImg`

#### 转换后结构如下

{{< alert text="具体结构示例文件，可移步：[labelImg_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/labelImg_dataset)" />}}

```text linenums="1"
labelImg_dataset
  ├── train
  │   ├── 000000000001.jpg
  │   ├── 000000000001.txt
  │   ├── 000000000002.jpg
  │   └── classes.txt
  └── val
      ├── 000000000001.jpg
      ├── 000000000001.txt
      └── classes.txt
```

#### labelImg 可视化

```bash linenums="1"
$ cd dataset/labelImg_dataset
$ labelImg train train/classes.txt

# or
$ labelImg val val/classes.txt
```
