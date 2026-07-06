#### 简介

将 YOLOv8 格式数据集转换为 YOLOv5 格式。

支持标注格式为矩形框和多边形框。

#### YOLOv8 数据结构如下

{{< alert text="具体结构示例文件，可移步：[yolov8_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/yolov8_dataset)" />}}

```text {linenos=table}
yolov8_dataset
├── images
│   ├── train
│   │   ├── 0dcddf72.jpg
│   │   └── images(3).jpg
│   └── val
│       ├── 8ae4af51.jpg
│       └── images(13).jpg
└── labels
    ├── train
    │   ├── 0dcddf72.txt
    │   └── images(3).txt
    └── val
        ├── 8ae4af51.txt
        └── images(13).txt
```

#### 转换

```bash {linenos=table}
yolov8_to_yolov5 --data_dir dataset/yolov5_dataset --mode_list train,val
```

- `--data_dir`: 数据集所在目录。示例为 `dataset/yolov5_dataset`
- `--save_dir`: 保存转换后的数据集目录。默认为 `dataset/yolov8_dataset_yolov5`
- `--mode_list`: 指定划分的数据集种类。(例如：`train,val,test` / `train,val`)
- `--yaml_path`: 指定的 yaml 配置文件，用于读取其中 `names` 类名

#### 转换后结构如下

{{< alert text="具体结构示例文件，可移步：[yolov5_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/yolov5_dataset)" />}}

```text {linenos=table}
yolov5_dataset
├── classes.txt
├── images
│   ├── images(13).jpg
│   └── images(3).jpg
├── labels
│   ├── images(13).txt
│   └── images(3).txt
├── train.txt
└── val.txt
```

<script src="https://giscus.app/client.js"
        data-repo="RapidAI/LabelConvert"
        data-repo-id="MDEwOlJlcG9zaXRvcnkzODkwNDExMDY="
        data-category="Q&A"
        data-category-id="DIC_kwDOFzBL0s4CYoY-"
        data-mapping="title"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="preferred_color_scheme"
        data-lang="zh-CN"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
</script>
