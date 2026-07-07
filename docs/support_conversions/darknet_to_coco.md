---
comments: true
---

#### 简介

将 Darnet 格式数据集转化为 COCO 格式数据集。

#### Darknet 结构如下

!!! tip

    具体结构示例文件，可移步：[darknet_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/darknet_dataset)

```text linenums="1"
darknet_dataset
├── class.names
├── gen_config.data
├── gen_train.txt
├── gen_valid.txt
└── images
    ├── train
    └── valid
```

#### 转换

```bash linenums="1"
darknet_to_coco --data_dir dataset/darknet_dataset
```

- `--data_dir`: COCO 格式数据集所在目录。示例为 `dataset/darknet_dataset`
- `--save_dir`: 保存转换后的数据集目录。默认为 `dataset/darknet_dataset_coco`

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
