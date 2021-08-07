# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File: coco_visual.py
import json
import random
import os
import argparse

import cv2


def visualization_bbox(num_image, json_path, img_path):
    with open(json_path) as annos:
        annotation_json = json.load(annos)

    print('the annotation_json num_key is:',len(annotation_json))  # 统计json文件的关键字长度
    print('the annotation_json key is:', annotation_json.keys()) # 读出json文件的关键字
    print('the annotation_json num_images is:', len(annotation_json['images'])) # json文件中包含的图片数量

    # 获取所有类别数
    categories = annotation_json['categories']
    categories_dict = {c['id']:c['name'] for c in categories}
    class_nums = len(categories_dict.keys())
    color = [(random.randint(0, 255), random.randint(0, 255),
              random.randint(0, 255)) for _ in range(class_nums)]

    # 读取图像
    image_name = annotation_json['images'][num_image - 1]['file_name']
    img_id = annotation_json['images'][num_image - 1]['id']
    image_path = os.path.join(img_path, str(image_name).zfill(5))
    image = cv2.imread(image_path, 1)

    annotations = annotation_json['annotations']
    num_bbox = 0
    for anno in annotations:
        if  anno['image_id'] == img_id:
            num_bbox = num_bbox + 1

            class_id = anno['category_id']
            class_name = categories_dict[class_id]
            class_color = color[class_id-1]

            # 绘制边框
            x, y, w, h = list(map(int, anno['bbox']))
            cv2.rectangle(image, (int(x), int(y)),
                          (int(x + w), int(y + h)),
                          class_color, 2)
            # 绘制文本
            font_size = 0.7
            txt_size = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX,
                                       font_size, 1)[0]
            cv2.rectangle(image, (x, y + 1),
                          (x + txt_size[0] + 10, y - int(2 * txt_size[1])),
                          class_color, -1)
            cv2.putText(image, class_name, (x + 5, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        font_size, (255, 255, 255), 1)

    print('The unm_bbox of the display image is:', num_bbox)

    cv2.namedWindow(image_name, 0)
    cv2.resizeWindow(image_name, 1000, 1000)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--vis_num', type=int, default=1,
                        help="可视化哪一张")
    parser.add_argument('--json_path', type=str, required=True)
    parser.add_argument('--img_dir', type=str, required=True)
    args = parser.parse_args()

    visualization_bbox(args.vis_num, args.json_path, args.img_dir)
