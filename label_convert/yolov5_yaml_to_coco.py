# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import json
import shutil
import time
import warnings
from pathlib import Path
from typing import List, Union

import cv2
import numpy as np
import yaml
from tqdm import tqdm


class YOLOv5CfgToCOCO:
    def __init__(
        self,
        yaml_path: Union[str, Path, None] = None,
        save_dir: Union[str, Path, None] = None,
    ):
        if yaml_path is None:
            raise ValueError("yaml_path must not be empty!")

        self.verify_exists(yaml_path)
        with open(yaml_path, "r", encoding="utf-8") as f:
            self.cfg = yaml.safe_load(f)

        data_dir = self.cfg.get("path", None)
        if data_dir is None:
            data_dir = ""

        self.data_dir = Path(data_dir)
        self.train_dir = self.data_dir / self.cfg.get("train")
        self.val_dir = self.data_dir / self.cfg.get("val")

        nc = self.cfg.get("nc")
        self.names = self.cfg.get("names")
        assert nc == len(self.names)

        if save_dir is None:
            save_dir = self.data_dir.parent / f"{self.data_dir.name}_coco"
        self.save_dir = Path(save_dir)

        self.coco_train_dir = self.save_dir / "train2017"
        self.coco_val_dir = self.save_dir / "val2017"
        self.anno_dir = self.save_dir / "annotations"

        self.train_json = self.anno_dir / f"instances_{self.coco_train_dir.name}.json"
        self.val_json = self.anno_dir / f"instances_{self.coco_val_dir.name}.json"

        self.mkdir(self.coco_train_dir)
        self.mkdir(self.coco_val_dir)
        self.mkdir(self.anno_dir)

        self._init_json()

        self.IMG_FORMATS = [
            "bmp",
            "dng",
            "jpeg",
            "jpg",
            "mpo",
            "png",
            "tif",
            "tiff",
            "webp",
        ]

    def __call__(self):
        train_imgs = self.get_img_list(self.train_dir)
        self.gen_dataset(train_imgs, self.coco_train_dir, self.train_json, mode="train")

        val_imgs = self.get_img_list(self.val_dir)
        self.gen_dataset(val_imgs, self.coco_val_dir, self.val_json, mode="val")

        print(f"Successfully convert, detail in {self.save_dir}")

    def _init_json(self):
        self.type = "instances"
        self.annotation_id = 1
        self.categories = self._get_category()

        self.cur_year = time.strftime("%Y", time.localtime(time.time()))
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

    def get_img_list(self, data_dir: Path):
        return list(data_dir.rglob("*.*"))

    def _get_category(self):
        categories = []
        for i, category in enumerate(self.names, start=1):
            categories.append(
                {
                    "supercategory": category,
                    "id": i,
                    "name": category,
                }
            )
        return categories

    def gen_dataset(self, img_paths, target_img_path, target_json, mode):
        images, annotations = [], []
        for img_id, img_path in enumerate(tqdm(img_paths, desc=mode), 1):
            self.verify_exists(img_path)
            img = cv2.imread(str(img_path))
            height, width = img.shape[:2]

            dest_file_name = f"{img_id:012d}.jpg"
            save_img_path = target_img_path / dest_file_name

            if img_path.suffix.lower() == ".jpg":
                shutil.copyfile(img_path, save_img_path)
            else:
                cv2.imwrite(str(save_img_path), img)

            images.append(
                {
                    "date_captured": "2021",
                    "file_name": dest_file_name,
                    "id": img_id,
                    "height": height,
                    "width": width,
                }
            )

            label_name = f"{img_path.stem}.txt"
            label_path = self.data_dir / "labels" / img_path.parent.name / label_name
            if not label_path.exists():
                warnings.warn(f"{label_path} not exists. Skip")
                continue

            new_anno = self.read_annotation(label_path, img_id, height, width)
            if len(new_anno) <= 0:
                warnings.warn(f"{label_path} is empty. Skip")
                continue
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

    def read_annotation(self, label_path, img_id, height, width):
        annotation = []
        all_info = self.read_txt(label_path)
        for label_info in all_info:
            label_info = label_info.split(" ")
            label_len = len(label_info)
            if label_len < 5:
                continue

            category_id, vertex_info = label_info[0], label_info[1:]

            point_nums = len(vertex_info)
            if point_nums == 4:
                segmentation, bbox, area = self.get_annotation_from_rectangle(
                    vertex_info, height, width
                )
            elif point_nums > 4:
                segmentation, bbox, area = self.get_annotation_from_poly(
                    vertex_info, height, width
                )
            else:
                warnings.warn("The nums of points are less than 4. Skip")
                continue

            annotation.append(
                {
                    "segmentation": segmentation,
                    "area": area,
                    "iscrowd": 0,
                    "image_id": img_id,
                    "bbox": bbox,
                    "category_id": int(category_id) + 1,
                    "id": self.annotation_id,
                }
            )
            self.annotation_id += 1
        return annotation

    @staticmethod
    def get_annotation_from_rectangle(vertex_info, height, width):
        cx, cy, w, h = [float(i) for i in vertex_info]

        cx = cx * width
        cy = cy * height
        box_w = w * width
        box_h = h * height

        x0 = max(cx - box_w / 2, 0)
        y0 = max(cy - box_h / 2, 0)
        x1 = min(x0 + box_w, width)
        y1 = min(y0 + box_h, height)

        segmentation = [[x0, y0, x1, y0, x1, y1, x0, y1]]
        bbox = [x0, y0, box_w, box_h]
        area = box_w * box_h
        return segmentation, bbox, area

    @staticmethod
    def get_annotation_from_poly(vertex_info: List[str], height, width):
        points = np.array(vertex_info).astype(np.float64).reshape(-1, 2)

        new_points = np.copy(points)
        new_points[:, 0] = points[:, 0] * width
        new_points[:, 1] = points[:, 1] * height

        segmentation = new_points.tolist()

        x0, y0 = np.min(new_points, axis=0)
        x1, y1 = np.max(new_points, axis=0)
        box_w = x1 - x0
        box_h = y1 - y0
        bbox = [x0, y0, box_w, box_h]

        area = box_w * box_h
        return segmentation, bbox, area

    @staticmethod
    def read_txt(txt_path):
        with open(str(txt_path), "r", encoding="utf-8") as f:
            data = list(map(lambda x: x.rstrip("\n"), f))
        return data

    @staticmethod
    def mkdir(dir_path):
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def verify_exists(file_path):
        file_path = Path(file_path).resolve()
        if not file_path.exists():
            raise FileNotFoundError(f"The {file_path} is not exists!!!")


def main():
    parser = argparse.ArgumentParser("Datasets converter from YOLOv5 YAML to COCO")
    parser.add_argument(
        "--yaml_path",
        type=str,
        default="tests/test_files/crack.v1i.yolov7pytorch/data.yaml",
        help="Dataset cfg file",
    )
    parser.add_argument("--save_dir", type=str, default=None)
    args = parser.parse_args()

    converter = YOLOv5CfgToCOCO(args.yaml_path, args.save_dir)
    converter()


if __name__ == "__main__":
    main()
