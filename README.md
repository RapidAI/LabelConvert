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
- YOLOV5训练格式目录结构（详情参见`dataset/YOLOV5`）：
  ```text
  YOLOV5
  ├── classes.txt
  ├── xxxx
  │   ├── images
  │   └── labels
  ├── train.txt
  └── val.txt
  ```

- 转换
  ```shell
  python yolov5_2_coco.py --dir_path dataset/YOLOV5
  ```

#### 可视化COCO格式标注格式
  ```shell
  python coco_visual.py --vis_num 1 \
                        --json_path dataset/YOLOV5_COCO_format/annotations/instances_train2017.json \
                        --img_dir dataset/YOLOV5_COCO_format/train2017
  ```

#### 相关资料
- [MSCOCO数据标注详解](https://blog.csdn.net/wc781708249/article/details/79603522)
