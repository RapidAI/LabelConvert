## YOLO2COCO
---
#### YOLOV5格式数据 → COCO
- 可以将一些背景图像加入到训练中，具体做法是：直接将背景图像放入`backgroud_images`目录即可。
- 转换程序会自动扫描该目录，添加到训练集中，可以无缝集成后续YOLOX的训练。
- YOLOV5训练格式目录结构（详情参见`dataset/YOLOV5`）：
    ```text
    YOLOV5
    ├── classes.txt
    ├── background_images  # 背景图像，一般是和要检测的对象容易混淆的图像
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

- 转换
    ```shell
  python yolov5_2_coco.py --dir_path dataset/YOLOV5 --mode_list train,val
  ```
  - `--dir_path`：整理好的数据集所在目录
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

#### YOLOV5 YAML描述文件 → COCO
- YOLOV5 yaml 数据文件需要包含：
    ```text
    YOLOV5_yaml/
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

#### darknet格式数据 → COCO
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
  python darknet2coco.py --data_path dataset/darknet/gen_config.data
  ```

#### 可视化COCO格式下图像
```shell
python coco_visual.py --vis_num 1 \
                    --json_path dataset/YOLOV5_COCO_format/annotations/instances_train2017.json \
                    --img_dir dataset/YOLOV5_COCO_format/train2017
```

- `--vis_num`：指定要查看的图像索引
- `--json_path`：查看图像的json文件路径
- `--img_dir`: 查看图像所在的目录

#### 相关资料
- [MSCOCO数据标注详解](https://blog.csdn.net/wc781708249/article/details/79603522)
