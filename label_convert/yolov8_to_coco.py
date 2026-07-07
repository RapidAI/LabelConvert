# -*- encoding: utf-8 -*-
# @Author: Lwen1243
# @Contact: 1198807618@qq.com
import argparse
import json
import shutil
import time
import warnings
from pathlib import Path
from typing import List, Tuple, Union

import cv2
import numpy as np
from tqdm import tqdm

ValueType = Union[str, Path, None]


class YOLOv8ToCOCO:
    def __init__(
        self,
        data_dir: ValueType = None,
        save_dir: ValueType = None,
        yaml_path: ValueType = None,
    ):
        if data_dir is None:
            raise ValueError("data_dir must not be None")

        self.data_dir = Path(data_dir)
        self.verify_exists(self.data_dir)

        self.img_dir = self.data_dir / "images"
        self.verify_exists(self.img_dir)

        self.label_dir = self.data_dir / "labels"
        self.verify_exists(self.label_dir)

        if save_dir is None:
            save_dir = self.data_dir.parent / f"{self.data_dir.name}_coco"

        self.save_dir = Path(save_dir)
        self.mkdir(self.save_dir)

        self.yaml_path = yaml_path

        self._init_json()

    def __call__(self, mode_list: Tuple[str] = ("train", "val")):
        if not mode_list:
            raise ValueError("mode_list is empty!!")

        for mode in mode_list:
            mode_img_dir = self.img_dir / mode
            self.verify_exists(mode_img_dir)
            img_list = list(mode_img_dir.iterdir())

            save_img_dir = self.save_dir / f"{mode}2017"
            self.mkdir(save_img_dir)

            anno_dir = self.save_dir / "annotations"
            self.mkdir(anno_dir)

            save_json_path = anno_dir / f"instances_{mode}2017.json"
            json_data = self.convert(img_list, save_img_dir, mode)

            self.write_json(save_json_path, json_data)
        print(f"Successfully convert, detail in {self.save_dir}")

    def _init_json(self):
        if self.yaml_path is not None:
            yaml_data = self.read_yaml(self.yaml_path)
            class_names = list(yaml_data["names"].values())
        else:
            class_names = self._get_class_names_from_labels()

        self.categories = self._get_category(class_names)

        self.type = "instances"
        self.annotation_id = 1

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

    def _get_class_names_from_labels(self):
        class_ids = set()
        for mode in ("train", "val"):
            mode_label_dir = self.label_dir / mode
            if not mode_label_dir.exists():
                continue

            for label_path in mode_label_dir.iterdir():
                if label_path.suffix != ".txt":
                    continue

                label_list = self.read_txt(str(label_path))
                for line in label_list:
                    if not line.strip():
                        continue

                    parts = line.strip().split()
                    if parts:
                        class_ids.add(int(parts[0]))

        if not class_ids:
            raise ValueError(
                "No class ids found in labels. "
                "Please provide a yaml_path with class names."
            )

        max_id = max(class_ids)
        class_names = [""] * (max_id + 1)
        for cid in class_ids:
            class_names[cid] = f"class_{cid}"

        return class_names

    def _get_category(self, class_names):
        categories = []
        for i, name in enumerate(class_names):
            if not name:
                continue

            categories.append({"supercategory": name, "id": i, "name": name})
        return categories

    def convert(self, img_list, save_img_dir, mode):
        images, annotations = [], []
        for img_id, img_path in enumerate(tqdm(img_list, desc=mode), 1):
            image_dict = self.get_image_info(img_path, img_id, save_img_dir)
            images.append(image_dict)

            mode_label_dir = self.label_dir / mode
            label_path = mode_label_dir / f"{img_path.stem}.txt"
            if not label_path.exists():
                warnings.warn(f"{label_path} not exists. Skip")
                continue

            annotation = self.read_annotation(
                label_path, img_id, image_dict["height"], image_dict["width"]
            )
            annotations.extend(annotation)

        json_data = {
            "info": self.info,
            "images": images,
            "licenses": self.licenses,
            "type": self.type,
            "annotations": annotations,
            "categories": self.categories,
        }
        return json_data

    def get_image_info(self, img_path, img_id, save_img_dir):
        img_path = Path(img_path)
        self.verify_exists(img_path)

        new_img_name = f"{img_id:012d}.jpg"
        save_img_path = save_img_dir / new_img_name

        img_src = cv2.imread(str(img_path))
        if img_src is None:
            raise ValueError(f"Failed to read image: {img_path}")

        if img_path.suffix.lower() == ".jpg":
            shutil.copyfile(img_path, save_img_path)
        else:
            cv2.imwrite(str(save_img_path), img_src)

        height, width = img_src.shape[:2]
        image_info = {
            "date_captured": self.cur_year,
            "file_name": new_img_name,
            "id": img_id,
            "height": height,
            "width": width,
        }
        return image_info

    def read_annotation(self, label_path: Path, img_id, height, width):
        annotation = []
        label_list = self.read_txt(str(label_path))
        for i, one_line in enumerate(label_list):
            label_info = one_line.split(" ")
            if len(label_info) < 5:
                warnings.warn(
                    f"The {i + 1} line of the {label_path} has been corrupted."
                )
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
    def verify_exists(file_path: Union[Path, str]):
        if not Path(file_path).exists():
            raise FileNotFoundError(f"The {file_path} is not exists!!!")

    @staticmethod
    def write_json(json_path, content: dict):
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False)

    @staticmethod
    def read_yaml(yaml_path):
        import yaml

        with open(yaml_path, "rb") as f:
            data = yaml.load(f, Loader=yaml.Loader)
        return data


def main():
    parser = argparse.ArgumentParser("Datasets converter from YOLOv8 to COCO")
    parser.add_argument(
        "--data_dir",
        type=str,
        default="tests/test_files/yolov8_dataset",
        help="Dataset root path (contains images/ and labels/ subdirectories)",
    )
    parser.add_argument("--save_dir", type=str, default=None)
    parser.add_argument(
        "--mode_list", type=str, default="train,val", help="generate which mode"
    )
    parser.add_argument(
        "--yaml_path",
        type=str,
        default=None,
        help="YAML file path for class names (optional)",
    )
    args = parser.parse_args()

    converter = YOLOv8ToCOCO(args.data_dir, args.save_dir, args.yaml_path)
    converter(mode_list=args.mode_list.split(","))


if __name__ == "__main__":
    main()
