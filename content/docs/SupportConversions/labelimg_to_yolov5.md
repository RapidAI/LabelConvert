---
weight: 10
date: "2022-09-30"
draft: false
author: "SWHL"
title: "labelImg → YOLOv5"
icon: "circle"
toc: true
description: ""
publishdate: "2022-09-30"
---

#### 简介
将[labelImg](https://github.com/tzutalin/labelImg)标注的数据集格式转换为YOLO格式。


#### labelImg结构如下：

{{< alert text="具体结构示例文件，可移步：[labelImg_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/labelImg_dataset)" />}}

````text {linenos=table}
labelImg_dataset
├── classes.txt
├── images(13).jpg
├── images(13).txt
├── images(3).jpg
├── images(3).txt
├── images4.jpg
├── images4.txt
├── images5.jpg
├── images5.txt
├── images6.jpg
├── images7.jpg
└── images7.txt
````

#### 转换
```bash {linenos=table}
labelImg_to_yolov5 --data_dir dataset/labelImg_dataset \
                   --save_dir dataset/labelImg_dataset_output \
                   --val_ratio 0.2 \
                   --have_test \
                   --test_ratio 0.2
```

- `--data_dir`: labelme标注的数据所在路径，示例为`dataset/labelImg_dataset`
- `--save_dir`: 转换后数据存储路径，默认为`dataset/labelImg_dataset_publaynet`
- `--val_ratio`: 验证集所占比例，默认为总量的0.2
- `--have_test`: 是否划出测试集，默认为`False`，如果想要划分测试集，直接加上该参数即可。
- `--test_ratio`: 测试集的比例，默认为总量的0.2

#### 转换后结构如下：

{{< alert text="具体结构示例文件，可移步：[yolov5_dataset](https://github.com/RapidAI/LabelConvert/tree/main/tests/test_files/yolov5_dataset)" />}}


````text {linenos=table}
labelImg_dataset_output/
├── classes.txt
├── images
│   ├── images(13).jpg
│   ├── images(3).jpg
│   ├── images4.jpg
│   ├── images5.jpg
│   └── images7.jpg
├── labels
│   ├── images(13).txt
│   ├── images(3).txt
│   ├── images4.txt
│   ├── images5.txt
│   └── images7.txt
├── non_labels        # 这个是没有标签的图像目录
│   └── images6.jpg
├── test.txt
├── train.txt
└── val.txt
````

#### 进一步转换为COCO格式
```bash {linenos=table}
yolov5_to_coco --data_dir dataset/labellImg_dataset_output
````

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