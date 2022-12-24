## YOLO2COCO
简体中文 | [English](./docs/README_en.md)

<p align="left">
    <a href=""><img src="https://img.shields.io/badge/Python-3.6+-aff.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Win%2C%20Mac-pink.svg"></a>
    <a href="https://github.com/RapidAI/YOLO2COCO/graphs/contributors"><img src="https://img.shields.io/github/contributors/RapidAI/YOLO2COCO?color=9ea"></a>
    <a href="https://github.com/RapidAI/YOLO2COCO/stargazers"><img src="https://img.shields.io/github/stars/RapidAI/YOLO2COCO?color=ccf"></a>
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202-dfd.svg"></a>
</p>


#### labelImg标注yolo格式数据 → YOLOV5格式
<details>

  - 将[labelImg](https://github.com/tzutalin/labelImg)库标注的yolo数据格式一键转换为YOLOV5格式数据
  - labelImg标注数据目录结构如下（详情参见`dataset/labelImg_dataset`）：
    ```text
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
      ├── images6.jpg  # 注意这个是没有标注的
      ├── images7.jpg
      └── images7.txt
    ```
  - 转换
    ```shell
    python labelImg_2_yolov5.py --src_dir dataset/labelImg_dataset \
                                --out_dir dataset/labelImg_dataset_output \
                                --val_ratio 0.2 \
                                --have_test true \
                                --test_ratio 0.2
    ```
    - `--src_dir`：labelImg标注后所在目录
    - `--out_dir`： 转换之后的数据存放位置
    - `--val_ratio`：生成验证集占整个数据的比例，默认是`0.2`
    - `--have_test`：是否生成test部分数据，默认是`True`
    - `--test_ratio`：test数据整个数据百分比，默认是`0.2`

  - 转换后目录结构（详情参见`dataset/labelImg_dataset_output`）：
    ```text
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
      ├── non_labels        # 这是没有标注图像的目录，自行决定如何处置
      │   └── images6.jpg
      ├── test.txt
      ├── train.txt
      └── val.txt
    ```
  - 可以进一步直接对`dataset/labelImg_dataset_output`目录作转COCO的转换
    ```shell
    python yolov5_2_coco.py --data_dir dataset/lablelImg_dataset_output
    ```

</details>

#### COCO格式数据 → labelImg
<details>

- 将COCO格式数据一键转换为labelImg标注的yolo格式数据
- COCO格式数据目录结构如下（详情参见：`dataset/YOLOV5_COCO_format`）：
  ```text
  YOLOV5_COCO_format
    ├── annotations
    │   ├── instances_train2017.json
    │   └── instances_val2017.json
    ├── train2017
    │   ├── 000000000001.jpg
    │   └── 000000000002.jpg  # 这个是背景图像
    └── val2017
        └── 000000000001.jpg
  ```
- 转换
  ```bash
  python coco_2_labelImg.py --data_dir dataset/YOLOV5_COCO_format
  ```
  - `--data_dir`: COCO格式数据集所在目录
- 转换后目录结构（详情参见：`dataset/COCO_labelImg_format`）:
  ```text
  COCO_labelImg_format
    ├── train
    │   ├── 000000000001.jpg
    │   ├── 000000000001.txt
    │   |-- 000000000002.jpg
    │   └── classes.txt
    └── val
        ├── 000000000001.jpg
        ├── 000000000001.txt
        └── classes.txt
  ```
- 对转换之后的目录，可以直接用`labelImg`库直接打开，更改标注，具体命令如下：
  ```shell
  $ cd dataset/COCO_labelImg_format
  $ labelImg train train/classes.txt

  # or
  $ labelImg val val/classes.txt
  ```
</details>

#### YOLOV5格式数据 → COCO
<details>

  - 可以将一些背景图像加入到训练中，具体做法是：直接将背景图像放入`backgroud_images`目录即可。
  - 转换程序会自动扫描该目录，添加到训练集中，可以无缝集成后续[YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)的训练。
  - YOLOV5训练格式目录结构（详情参见`dataset/YOLOV5`）：
      ```text
      YOLOV5
      ├── classes.txt
      ├── background_images  # 一般是和要检测的对象容易混淆的图像
      │   └── bg1.jpeg
      ├── images
      │   ├── images(13).jpg
      │   └── images(3).jpg
      ├── labels
      │   ├── images(13).txt
      │   └── images(3).txt
      ├── train.txt
      └── val.txt
      ```
  - **train.txt**和**val.txt**中图像路径，以下两种均可：
    - 相对于**根目录**的路径
      ```text
      dataset/YOLOV5/images/images(3).jpg
      ```
    - 相对于**dataset/YOLOV5**的相对路径
      ```text
      images/images(3).jpg
      ```
  - 转换
      ```shell
    python yolov5_2_coco.py --data_dir dataset/YOLOV5 --mode_list train,val
    ```
    - `--data_dir`：整理好的数据集所在目录
    - `--mode_list`：指定生成的json，前提是要有对应的txt文件，可单独指定。（e.g. `train,val,test`）

  - 转换后目录结构（详情参见`dataset/YOLOV5_COCO_format`）：
    ```text
    YOLOV5_COCO_format
    ├── annotations
    │   ├── instances_train2017.json
    │   └── instances_val2017.json
    ├── train2017
    │   ├── 000000000001.jpg
    │   └── 000000000002.jpg  # 这个是背景图像
    └── val2017
        └── 000000000001.jpg
    ```
</details>

#### YOLOV5 YAML描述文件 → COCO
<details>

  - YOLOV5 yaml 数据文件目录结构如下（详情参见`dataset/YOLOV5_yaml`）：
      ```text
      YOLOV5_yaml
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

  - 转换
    ```shell
    python yolov5_yaml_2_coco.py --yaml_path dataset/YOLOV5_yaml/sample.yaml
    ```
</details>

#### darknet格式数据 → COCO
<details>

  - darknet训练数据目录结构（详情参见`dataset/darknet`）：
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

  - 转换
    ```shell
    python darknet_2_coco.py --data_path dataset/darknet/gen_config.data
    ```
</details>

#### 可视化COCO格式下图像
<details>

```shell
python coco_visual.py --vis_num 1 \
                    --json_path dataset/YOLOV5_COCO_format/annotations/instances_train2017.json \
                    --img_dir dataset/YOLOV5_COCO_format/train2017
```

- `--vis_num`：指定要查看的图像索引
- `--json_path`：查看图像的json文件路径
- `--img_dir`: 查看图像所在的目录

</details>

#### COCO格式Object Instance示例
<details>

```json
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
        "image_id": 1,  // 对应images中的id
        "bbox": [18.00, 2.99, 87.00, 86.00],  // [x, y, w, h]其中(x,y)是左上角的值，w,h是框的宽和高
        "category_id": 1,  // 对应categories中的ID
        "id": 1  // 唯一区分不同标注实例的编号
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

</details>

#### 相关资料
- [MSCOCO数据标注详解](https://blog.csdn.net/wc781708249/article/details/79603522)
