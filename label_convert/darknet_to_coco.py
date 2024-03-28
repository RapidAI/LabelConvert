# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import configparser as cfg
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Union

import cv2

ValueType = Union[str, Path, None]


class DarknetToCOCO:
    def __init__(
        self,
        data_dir: ValueType = None,
        save_dir: ValueType = None,
    ):
        self.data_dir = Path(data_dir)
        self.verify_exists(self.data_dir)

        self.config_path = self.data_dir / "gen_config.data"
        self.config = self.load_cfg()

        if save_dir is None:
            save_dir = self.data_dir.parent / f"{self.data_dir.name}_coco"
        self.save_dir = Path(save_dir)
        self.mkdir(self.save_dir)

        anno_dir = self.save_dir / "annotations"
        self.mkdir(anno_dir)

        self.train_json = anno_dir / "instances_train2017.json"
        self.val_json = anno_dir / "instances_val2017.json"

        self.train2017_dir = self.save_dir / "train2017"
        self.val2017_dir = self.save_dir / "val2017"
        self.mkdir(self.train2017_dir)
        self.mkdir(self.val2017_dir)

        self.type = "instances"
        self.categories = []
        self.annotation_id = 1

        self.cur_year = datetime.strftime(datetime.now(), "%Y")
        self.info = {
            "year": int(self.cur_year),
            "version": "1.0",
            "description": "For object detection",
            "date_created": self.cur_year,
        }
        self.licenses = [
            {
                "id": 1,
                "name": "Apache License v2.0",
                "url": "https://github.com/RapidAI/LabelConvert/LICENSE",
            }
        ]

    def load_cfg(self):
        config = cfg.RawConfigParser()
        with open(self.config_path, "r", encoding="utf-8") as f:
            file_content = "[dummy_section]\n" + f.read()
        config.read_string(file_content)
        return config

    def __call__(self):
        train_path = self.data_dir / self.get_key_value("train")

        cls_name_path = self.data_dir / self.get_key_value("names")
        cls_name_list = self.read_txt(cls_name_path)
        self.get_category(cls_name_list)

        train_imgs = self.read_txt(train_path)
        self.gen_dataset(train_imgs, self.train2017_dir, self.train_json)

        val_imgs = None
        val_path = self.data_dir / self.get_key_value("valid")
        if val_path is not None:
            val_imgs = self.read_txt(val_path)
            self.gen_dataset(val_imgs, self.val2017_dir, self.val_json)

        print(f"Successfully convert, detail in {self.save_dir}")

    def get_key_value(self, key):
        try:
            return self.config.get("dummy_section", key)
        except Exception:
            return None

    def get_category(self, cls_name_list: List[str]) -> None:
        for i, category in enumerate(cls_name_list, 1):
            self.categories.append(
                {
                    "id": i,
                    "name": category,
                    "supercategory": category,
                }
            )

    def gen_dataset(self, img_paths, save_dir: Path, target_json):
        images, annotations = [], []
        for img_id, img_path in enumerate(img_paths, 1):
            img_full_path: Path = self.data_dir / img_path
            if not img_full_path.exists():
                continue

            save_img_name = f"{img_id:012d}{img_full_path.suffix}"
            save_img_path = save_dir / save_img_name

            img = cv2.imread(str(img_full_path))
            if img_full_path.suffix.lower() == ".jpg":
                shutil.copyfile(img_full_path, save_img_path)
            else:
                cv2.imwrite(str(save_img_path), img)

            height, width = img.shape[:2]
            images.append(
                {
                    "date_captured": str(self.cur_year),
                    "file_name": save_img_name,
                    "id": img_id,
                    "height": height,
                    "width": width,
                }
            )

            txt_path = img_full_path.with_suffix(".txt")
            if txt_path.exists():
                new_anno = self.read_annotation(txt_path, img_id, height, width)
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

    def read_annotation(self, txt_path, img_id, height, width):
        annotation = []
        if not Path(txt_path).exists():
            return {}, 0

        with open(txt_path, "r", encoding="utf-8") as f:
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

    def _get_annotation(self, vertex_info, height, width):
        """
        derived from https://github.com/zhiqwang/yolov5-rt-stack/blob/master/yolort/utils/yolo2coco.py
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

    @staticmethod
    def verify_exists(file_path: Union[str, Path]) -> None:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"The {file_path} is not exists!!!")

    @staticmethod
    def mkdir(dir_path: Union[str, Path]):
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def read_txt(txt_path: str) -> List:
        if not isinstance(txt_path, str):
            txt_path = str(txt_path)

        with open(txt_path, "r", encoding="utf-8") as f:
            data = list(map(lambda x: x.rstrip("\n"), f))
        return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_dir",
        default="dataset/darknet_dataset",
        help="Dataset root path",
    )
    args = parser.parse_args()

    converter = DarknetToCOCO(args.data_dir)
    converter()
