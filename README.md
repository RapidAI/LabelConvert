#### darknet格式数据→COCO
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

#### YOLOV5格式数据→COCO
- 值得一提的是，由标注软件[labelImg](https://github.com/tzutalin/labelImg)标注所得yolo格式数据，也可由该脚本做转换。前提是满足以下数据目录结构。
- YOLOV5训练格式目录结构（详情参见`dataset/YOLOV5`）：
    ```text
    YOLOV5
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

- 转换
  ```shell
  python yolov5_2_coco.py --dir_path dataset/YOLOV5
  ```
- 转换后目录结构（详情参见`dataset/YOLOV5_COCO_format`）：
    ```text
    YOLOV5_COCO_format
    ├── annotations
    │   ├── instances_train2017.json
    │   └── instances_val2017.json
    ├── train2017
    │   └── 000000000001.jpg
    └── val2017
        └── 000000000001.jpg
    ```

#### YOLOV5 yaml数据描述文件转→COCO

- YOLOV5 yaml 数据文件需要包含：
    ```text
    YOLOV5 yaml
    ├── path(str, the root path)
    ├── train(Train sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..])
    ├── val(val sets, similar as train)

    ```

- 转换
  ```shell
  python yolov5_cfgfile_2_coco.py --cfg_file dataset/sample.yaml
  ```

#### 可视化COCO格式标注格式
  ```shell
  python coco_visual.py --vis_num 1 \
                        --json_path dataset/YOLOV5_COCO_format/annotations/instances_train2017.json \
                        --img_dir dataset/YOLOV5_COCO_format/train2017
  ```

#### 相关资料
- [MSCOCO数据标注详解](https://blog.csdn.net/wc781708249/article/details/79603522)
