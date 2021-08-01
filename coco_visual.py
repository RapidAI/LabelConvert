# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File: coco_visual.py
import json
import os
import argparse

import cv2


def visualization_bbox(num_image, json_path, img_path):
    # 需要画的第num副图片， 对应的json路径和图片路径
    with open(json_path) as annos:
        annotation_json = json.load(annos)

    print('the annotation_json num_key is:',len(annotation_json))  # 统计json文件的关键字长度
    print('the annotation_json key is:', annotation_json.keys()) # 读出json文件的关键字
    print('the annotation_json num_images is:', len(annotation_json['images'])) # json文件中包含的图片数量

    image_name = annotation_json['images'][num_image - 1]['file_name']  # 读取图片名
    id = annotation_json['images'][num_image - 1]['id']  # 读取图片id

    image_path = os.path.join(img_path, str(image_name).zfill(5)) # 拼接图像路径
    image = cv2.imread(image_path, 1)  # 保持原始格式的方式读取图像
    num_bbox = 0  # 统计一幅图片中bbox的数量
    len_anno=len(annotation_json['annotations'][::])
    for i in range(len_anno):
        if  annotation_json['annotations'][i]['image_id'] == id:
            num_bbox = num_bbox + 1
            x, y, w, h = annotation_json['annotations'][i]['bbox']  # 读取边框
            image = cv2.rectangle(image, (int(x), int(y)),
                                  (int(x + w), int(y + h)), (0, 255, 255), 2)

    print('The unm_bbox of the display image is:', num_bbox)

    # 显示方式1：用plt.imshow()显示
    # plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #绘制图像，将CV的BGR换成RGB
    # plt.show() #显示图像

    # 显示方式2：用cv2.imshow()显示
    cv2.namedWindow(image_name, 0)  # 创建窗口
    cv2.resizeWindow(image_name, 1000, 1000) # 创建500*500的窗口
    cv2.imshow(image_name, image)
    cv2.waitKey(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--json_path', type=str, required=True)
    parser.add_argument('--img_dir', type=str, required=True)
    args = parser.parse_args()

    visualization_bbox(1, args.json_path, args.img_dir)
