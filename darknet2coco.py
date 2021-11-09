# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File: darknet2coco.py
import argparse
import configparser as cfg
import json
import os
import shutil
from pathlib import Path

import cv2 as cv


class DARKNET2COCO:
    def __init__(self, genconfig_data):
        self.src_data = genconfig_data
        self.src = Path(self.src_data).parent
        self.dst = Path(self.src) / "coco_dataset"
        self.coco_train = "train2017"
        self.coco_valid = "val2017"
        self.coco_images = "images"
        self.coco_annotation = "annotations"
        self.coco_train_json = Path(self.dst) / self.coco_annotation / f'instances_{self.coco_train}.json'
        self.coco_valid_json = Path(self.dst) / self.coco_annotation / f'instances_{self.coco_valid}.json'
        self.type = 'instances'
        self.categories = []
        self.annotation_id = 1
        self.info = {
            'year': 2021,
            'version': '1.0',
            'description': 'For object detection',
            'date_created': '2021',
        }
        self.licenses = [{
            'id': 1,
            'name': 'Apache License v2.0',
            'url': 'https://github.com/RapidAI/YOLO2COCO/LICENSE',
        }]

        if not Path(self.dst).is_dir():
            Path(self.dst).mkdir()

        if not Path(self.dst / self.coco_images).is_dir():
            Path(self.dst/self.coco_images).mkdir()

        if not (Path(self.dst)/self.coco_images / self.coco_train).is_dir():
            (Path(self.dst)/self.coco_images/self.coco_train).mkdir()

        if not Path(self.dst / self.coco_images / self.coco_valid).is_dir():
            (Path(self.dst)/self.coco_images/self.coco_valid).mkdir()

        if not (Path(self.dst) / self.coco_annotation).is_dir():
            (Path(self.dst)/self.coco_annotation).mkdir()

        if Path(self.src_data).is_file():
            self.ready = True
            self.initcfg()
        else:
            self.ready = False

    def initcfg(self):
        if not self.ready:
            return
        self.cnf = cfg.RawConfigParser()
        with open(self.src_data) as f:
            file_content = '[dummy_section]\n' + f.read()
        self.cnf.read_string(file_content)

    def getint(self, key):
        if not self.ready:
            return 0
        return int(self.cnf.get("dummy_section", key))

    def getstring(self, key):
        if not self.ready:
            return ""
        return self.cnf.get("dummy_section", key)

    def get_path(self, name):
        content = []
        with open(name) as f:
            allfiles = f.readlines()
        for file in allfiles:
            if not os.path.isabs(file):
                this_path = Path(self.src) / file.strip()
                content.append(str(this_path))
            else:
                content.append(file.strip())
        return content

    def get_list(self, name):
        content = []
        with open(name) as f:
            allfiles = f.readlines()
        for file in allfiles:
            content.append(file.strip())

        return content

    def _get_annotation(self, vertex_info, height, width):
        '''
        # derived from https://github.com/zhiqwang/yolov5-rt-stack/blob/master/yolort/utils/yolo2coco.py

        '''
        cx, cy, w, h = [float(i) for i in vertex_info]
        cx = cx * width
        cy = cy * height
        w = w * width
        h = h * height
        x = cx - w / 2
        y = cy - h / 2

        segmentation = [[x, y, x + w, y, x + w, y + h, x, y + h]]
        area = w * h

        bbox = [x, y, w, h]
        return segmentation, bbox, area

    def read_annotation(self, txtfile, img_id, height, width):
        annotation = []
        if not Path(txtfile).exists():
            return {}, 0
        with open(txtfile) as f:
            allinfo = f.readlines()

        for line in allinfo:
            label_info = line.replace('\n', '').replace('\r', '')
            label_info = label_info.strip().split(" ")
            if len(label_info) < 5:
                continue

            category_id, vertex_info = label_info[0], label_info[1:]

            segmentation, bbox, area = self._get_annotation(
                vertex_info, height, width)
            annotation.append({
                'segmentation': segmentation,
                'area': area,
                'iscrowd': 0,
                'image_id': img_id,
                'bbox': bbox,
                'category_id': int(int(category_id)+1),
                'id': self.annotation_id,
            })
            self.annotation_id += 1

        return annotation

    def get_category(self):
        for id, category in enumerate(self.name_lists, 1):
            self.categories.append({
                'id': id,
                'name': category,
                'supercategory': category,
            })

    def generate(self):
        self.classnum = self.getint("classes")
        self.train = Path(self.src_data).parent / \
            Path(self.getstring("train")).name
        self.valid = Path(self.src_data).parent / \
            Path(self.getstring("valid")).name
        self.names = Path(self.src_data).parent / \
            Path(self.getstring("names")).name

        self.train_files = self.get_path(self.train)
        if os.path.exists(self.valid):
            self.valid_files = self.get_path(self.valid)

        self.name_lists = self.get_list(self.names)
        self.get_category()

        dest_path_train = Path(self.dst) / self.coco_images / self.coco_train
        self.gen_dataset(self.train_files, dest_path_train,
                         self.coco_train_json)

        dest_path_valid = Path(self.dst) / self.coco_images / self.coco_valid
        if os.path.exists(self.valid):
            self.gen_dataset(self.valid_files, dest_path_valid,
                             self.coco_valid_json)

        print("The output directory is :", str(self.dst))

    def gen_dataset(self, file_lists, target_img_path, target_json):
        '''
        https://cocodataset.org/#format-data

        '''
        images = []
        annotations = []
        for img_id, file in enumerate(file_lists, 1):
            if not Path(file).exists():
                continue
            txt = str(Path(file).parent / Path(file).stem) + \
                ".txt"

            tmpname = str(img_id)
            prefix = "0"*(12 - len(tmpname))
            destfilename = prefix+tmpname+".jpg"
            imgsrc = cv.imread(file)  # 读取图片
            if Path(file).suffix.lower() == ".jpg":
                shutil.copyfile(file, target_img_path/destfilename)
            else:
                cv.imwrite(str(target_img_path/destfilename), imgsrc)
            # shutil.copyfile(file,target_img_path/ )

            image = imgsrc.shape  # 获取图片宽高及通道数
            height = image[0]
            width = image[1]
            images.append({
                'date_captured': '2021',
                'file_name': destfilename,
                'id': img_id,
                'height': height,
                'width': width,
            })

            if Path(txt).exists():
                new_anno = self.read_annotation(txt, img_id, height, width)
                if len(new_anno) > 0:
                    annotations.extend(new_anno)

        json_data = {
            'info': self.info,
            'images': images,
            'licenses': self.licenses,
            'type': self.type,
            'annotations': annotations,
            'categories': self.categories,
        }
        with open(target_json, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', default='data/getn_config.data',
                        help='Dataset root path')
    args = parser.parse_args()

    converter = DARKNET2COCO(args.data_path)
    converter.generate()
