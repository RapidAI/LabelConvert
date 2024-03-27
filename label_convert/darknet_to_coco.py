# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import configparser as cfg
import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Union

import cv2 as cv

ValueType = Union[str, Path, None]


class DarknetToCOCO:
    def __init__(self, config_path: ValueType = None, save_dir: ValueType = None):
        if config_path is None:
            raise ValueError("config_path must not be empty.")

        self.config_path = Path(config_path)
        self.data_dir = self.config_path.parent

        if save_dir is None:
            save_dir = self.data_dir.parent / f"{self.data_dir.name}_coco"
        self.save_dir = Path(save_dir)
        self.mkdir(self.save_dir)

        anno_dir = self.save_dir / "annotations"
        self.mkdir(anno_dir)

        self.train_json = anno_dir / "instances_train2017.json"
        self.val_json = anno_dir / "instances_val2017.json"

        img_dir = self.save_dir / "images"
        self.train2017_dir = img_dir / "train2017"
        self.val2017_dir = img_dir / "val2017"
        self.mkdir(self.train2017_dir)
        self.mkdir(self.val2017_dir)

        self.type = "instances"
        self.categories = []
        self.annotation_id = 1

        cur_year = datetime.strftime(datetime.now(), "%Y")
        self.info = {
            "year": int(cur_year),
            "version": "1.0",
            "description": "For object detection",
            "date_created": cur_year,
        }
        self.licenses = [
            {
                "id": 1,
                "name": "Apache License v2.0",
                "url": "https://github.com/RapidAI/LabelConvert/LICENSE",
            }
        ]

        if Path(self.config_path).is_file():
            self.ready = True
            self.initcfg()
        else:
            self.ready = False

    def initcfg(self):
        if not self.ready:
            return
        self.cnf = cfg.RawConfigParser()
        with open(self.config_path, "r", encoding="utf-8") as f:
            file_content = "[dummy_section]\n" + f.read()
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
        with open(name, "r", encoding="utf-8") as f:
            allfiles = f.readlines()
        for file in allfiles:
            if not os.path.isabs(file):
                this_path = Path(self.data_dir) / file.strip()
                content.append(str(this_path))
            else:
                content.append(file.strip())
        return content

    def get_list(self, name):
        content = []
        with open(name, "r", encoding="utf-8") as f:
            allfiles = f.readlines()
        for file in allfiles:
            content.append(file.strip())
        return content

    @staticmethod
    def verify_exists(file_path: Union[str, Path]) -> None:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"The {file_path} is not exists!!!")

    @staticmethod
    def mkdir(dir_path: Union[str, Path]):
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    def _get_annotation(self, vertex_info, height, width):
        """
        # derived from https://github.com/zhiqwang/yolov5-rt-stack/blob/master/yolort/utils/yolo2coco.py

        """
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

        with open(txtfile, "r", encoding="utf-8") as f:
            allinfo = f.readlines()

        for line in allinfo:
            label_info = line.replace("\n", "").replace("\r", "")
            label_info = label_info.strip().split(" ")
            if len(label_info) < 5:
                continue

            category_id, vertex_info = label_info[0], label_info[1:]

            segmentation, bbox, area = self._get_annotation(vertex_info, height, width)
            annotation.append(
                {
                    "segmentation": segmentation,
                    "area": area,
                    "iscrowd": 0,
                    "image_id": img_id,
                    "bbox": bbox,
                    "category_id": int(int(category_id) + 1),
                    "id": self.annotation_id,
                }
            )
            self.annotation_id += 1

        return annotation

    def get_category(self):
        for i, category in enumerate(self.name_lists, 1):
            self.categories.append(
                {
                    "id": i,
                    "name": category,
                    "supercategory": category,
                }
            )

    def generate(self):
        self.classnum = self.getint("classes")
        self.train = Path(self.config_path).parent / Path(self.getstring("train")).name
        self.valid = Path(self.config_path).parent / Path(self.getstring("valid")).name
        self.names = Path(self.config_path).parent / Path(self.getstring("names")).name

        self.train_files = self.get_path(self.train)
        if os.path.exists(self.valid):
            self.valid_files = self.get_path(self.valid)

        self.name_lists = self.get_list(self.names)
        self.get_category()

        self.gen_dataset(self.train_files, self.train2017_dir, self.train_json)

        if os.path.exists(self.valid):
            self.gen_dataset(self.valid_files, self.val2017_dir, self.valid_json)

        print("The output directory is :", str(self.save_dir))

    def gen_dataset(self, file_lists, target_img_path, target_json):
        """
        https://cocodataset.org/#format-data

        """
        images = []
        annotations = []
        for img_id, file in enumerate(file_lists, 1):
            if not Path(file).exists():
                continue

            txt = str(Path(file).parent / Path(file).stem) + ".txt"

            tmpname = str(img_id)
            prefix = "0" * (12 - len(tmpname))
            destfilename = prefix + tmpname + ".jpg"
            imgsrc = cv.imread(file)  # 读取图片
            if Path(file).suffix.lower() == ".jpg":
                shutil.copyfile(file, target_img_path / destfilename)
            else:
                cv.imwrite(str(target_img_path / destfilename), imgsrc)
            # shutil.copyfile(file,target_img_path/ )

            image = imgsrc.shape  # 获取图片宽高及通道数
            height = image[0]
            width = image[1]
            images.append(
                {
                    "date_captured": "2021",
                    "file_name": destfilename,
                    "id": img_id,
                    "height": height,
                    "width": width,
                }
            )

            if Path(txt).exists():
                new_anno = self.read_annotation(txt, img_id, height, width)
                if len(new_anno) > 0:
                    annotations.extend(new_anno)

        json_data = {
            "info": self.info,
            "images": images,
            "licenses": self.licenses,
            "type": self.type,
            "annotations": annotations,
            "categories": self.categories,
        }
        with open(target_json, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path",
        default="dataset/darknet_dataset/gen_config.data",
        help="Dataset root path",
    )
    args = parser.parse_args()

    converter = DarknetToCOCO(args.data_path)
    converter.generate()
