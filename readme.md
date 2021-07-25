本程序用于将darknet的训练数据转换为coco格式，以便让yolox 使用。



文档参见 ： [csdn博客](https://blog.csdn.net/znsoft/article/details/119059967)

[YoloX 原始仓库](https://github.com/Megvii-BaseDetection/YOLOX)

[yolox 官方 自有数据训练方法](https://github.com/Megvii-BaseDetection/YOLOX/blob/main/docs/train_custom_data.md)





资料-  coco voc 格式 : http://www.xyu.ink/3612.html

coco 数据集格式快速训练 方法 for YOLOX

## clone yolox


## 



## 命令行
python tools/train.py -n yolox-s -d 1 -b 8 --fp16 -o yolox-m  yolox-l yolox-x  yolox_s

d 1表示一块显卡， -b 8 表示批大小，如果多块卡，这儿的8要换成  显卡数＊８
