[简体中文](./docs/README_zh.md) | English

<div align="center">
  <img src="https://github.com/RapidAI/YOLO2COCO/releases/download/v0/LabelConvertv3.png" width="55%" height="55%"/>
</div>

## LabelConvert

<p align="left">
    <a href=""><img src="https://img.shields.io/badge/Python-3.6+-aff.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Win%2C%20Mac-pink.svg"></a>
    <a href="https://github.com/RapidAI/YOLO2COCO/graphs/contributors"><img src="https://img.shields.io/github/contributors/RapidAI/YOLO2COCO?color=9ea"></a>
    <a href="https://github.com/RapidAI/YOLO2COCO/stargazers"><img src="https://img.shields.io/github/stars/RapidAI/YOLO2COCO?color=ccf" ></a>
    <a href=". /LICENSE"><img src="https://img.shields.io/badge/License-Apache%202-dfd.svg"></a>
    <a href="https://semver.org/"><img alt="SemVer2.0" src="https://img.shields.io/badge/SemVer-2.0-brightgreen"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

- A dataset format conversion tool for object detection and image segmentation, which supports mutual conversion between **labelme, labelImg tools and YOLO, VOC, and COCO** dataset formats.

#### labelImg label data → YOLOV5 format
<details>
    <summary>Click to expand</summary>

- Convert the yolo data format marked by the [labelImg](https://github.com/tzutalin/labelImg) library to YOLOV5 format data with one click.
- The labelImg label data directory structure is as follows (see `dataset/labelImg_dataset` for details):
  ````text
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
- Convert
    ```shell
    python labelImg_2_yolov5.py --src_dir dataset/labelImg_dataset \
                                --out_dir dataset/labelImg_dataset_output \
                                --val_ratio 0.2 \
                                --have_test true \
                                --test_ratio 0.2
    ```
    - `--src_dir`: the directory where labelImg is stored after labeling.
    - `--out_dir`: the location where the data is stored after conversion.
    - `--val_ratio`: the ratio of the generated validation set to the whole data, default is `0.2`.
    - `--have_test`: whether to generate the test part of the data, the default is `True`.
    - `--test_ratio`: percentage of the whole data of the test data, default is `0.2`.

- Converted directory structure (see `dataset/labelImg_dataset_output` for details):
  ````text
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
    ├── non_labels        # This is the catalog without the labeled images.
    │   └── images6.jpg
    ├── test.txt
    ├── train.txt
    └── val.txt
  ````
- You can further directly convert the `dataset/labelImg_dataset_output` directory to COCO
  ```shell
  python yolov5_2_coco.py --data_dir dataset/labellImg_dataset_output
  ````
</details>

#### COCO format data → labelImg yolo format
<details>
    <summary>Click to expand</summary>

- One-click conversion of COCO format data to labelImg labeled yolo format data.
- COCO format directory structure（see `dataset/YOLOV5_COCO_format` for details）：
  ```text
  YOLOV5_COCO_format
    ├── annotations
    │   ├── instances_train2017.json
    │   └── instances_val2017.json
    ├── train2017
    │   ├── 000000000001.jpg
    │   └── 000000000002.jpg
    └── val2017
        └── 000000000001.jpg
  ```
- Convert
  ```bash
  python coco_2_labelImg.py --data_dir dataset/YOLOV5_COCO_format
  ```
  - `--data_dir`: the directory where the COCO format dataset is located. Default is `dataset/YOLOV5_COCO_format`.
- Converted directory structure (see `dataset/COCO_labelImg_format` for details):
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
- For the converted directory, you can directly use the [labelImg](https://github.com/tzutalin/labelImg)  library to open it directly and change the label. The specific commands are as follows:
  ```shell
  $ cd dataset/COCO_labelImg_format
  $ labelImg train train/classes.txt

  # or
  $ labelImg val val/classes.txt
  ```
</details>

#### YOLOV5 format data → COCO
<details>
    <summary>Click to expand</summary>

- Some background images can be added to the training by directly placing them into the `backgroud_images` directory.
- The conversion program will automatically scan this directory and add it to the training set, allowing seamless integration with subsequent [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) training.
- YOLOV5 training format directory structure (see `dataset/YOLOV5` for details).
    ```text
    YOLOV5
    ├── classes.txt
    ├── background_images  # usually images that are easily confused with the object to be detected
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
- The image paths in train.txt and val.txt can be either:
  - Path relative to **root directory**:
      ```text
      dataset/YOLOV5/images/images(3).jpg
      ```
  - Path relative to **dataset/YOLOV5**:
      ```text
      images/images(3).jpg
      ```
- Convert
    ```shell
  python yolov5_2_coco.py --data_dir dataset/YOLOV5 --mode_list train,val
  ```
  - `--data_dir`: the directory where the collated dataset is located
  - `--mode_list`: specify the generated json, provided that there is a corresponding txt file, which can be specified separately. (e.g. `train,val,test`)

- The structure of the converted directory (see `dataset/YOLOV5_COCO_format` for details)
    ```text
    YOLOV5_COCO_format
    ├── annotations
    │   ├── instances_train2017.json
    │   └── instances_val2017.json
    ├── train2017
    │   ├── 000000000001.jpg
    │   └── 000000000002.jpg  # This is the background image.
    └── val2017
        └── 000000000001.jpg
    ```
</details>

#### YOLOV5 YAML description file → COCO
<details>
    <summary>Click to expand</summary>

- The YOLOV5 yaml data file needs to contain.
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

- Convert
  ```shell
  python yolov5_yaml_2_coco.py --yaml_path dataset/YOLOV5_yaml/sample.yaml
  ```
</details>

#### darknet format data → COCO
<details>

- Darknet training data directory structure (see `dataset/darknet` for details).
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

- Convert
  ```shell
  python darknet_2_coco.py --data_path dataset/darknet/gen_config.data
  ```
</details>

#### Visualize images in COCO format
<details>
    <summary>Click to expand</summary>

```shell
python coco_visual.py --vis_num 1 \
                    --json_path dataset/YOLOV5_COCO_format/annotations/instances_train2017.json \
                    --img_dir dataset/YOLOV5_COCO_format/train2017
```

- `--vis_num`: specify the index of the image to be viewed
- `--json_path`: path to the json file of the image to view
- `--img_dir`: view the directory where the image is located

</details>

#### Object Instance demo of COCO
<details>
    <summary>Click to expand</summary>

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
</details>

#### Related information
- [MSCOCO Data Annotation Details](https://blog.csdn.net/wc781708249/article/details/79603522)
