# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import json
import random
import shutil
import time
from pathlib import Path
from typing import List, Union

import cv2
import numpy as np
from tqdm import tqdm

ValueType = Union[str, Path, None]
RECTANGLE = "rectangle"
POLYGON = "polygon"


class LabelmeToCOCO:
    def __init__(
        self,
        data_dir: ValueType = None,
        save_dir: ValueType = None,
        val_ratio: float = 0.2,
        have_test: bool = False,
        test_ratio: float = 0.2,
    ):
        if data_dir is None:
            raise ValueError("data_dir must not be None")
        self.data_dir = Path(data_dir)
        self.verify_exists(self.data_dir)

        self.val_ratio = val_ratio
        self.test_ratio = test_ratio
        self.have_test = have_test

        self.verify_exists(self.data_dir)

        if save_dir is None:
            save_dir = self.data_dir.parent / f"{Path(self.data_dir).name}_coco"
        self.save_dir = Path(save_dir)
        self.mkdir(self.save_dir)

        self.anno_dir = self.save_dir / "annotations"
        self.mkdir(self.anno_dir)

        self.train_dir = self.save_dir / "train2017"
        self.mkdir(self.train_dir)

        self.val_dir = self.save_dir / "val2017"
        self.mkdir(self.val_dir)

        self.test_dir = None
        if have_test:
            self.test_dir = self.save_dir / "test2017"
            self.mkdir(self.test_dir)

        self.cur_year = time.strftime("%Y", time.localtime(time.time()))

        self.cls_to_idx = {}
        self.object_id = 1

        self.categories = self._get_category()

    def __call__(
        self,
    ):
        img_list = self.get_img_list()
        if not img_list:
            raise ValueError(f"{self.data_dir} is empty!")

        img_list = self.gen_image_label_dir(img_list)
        split_list = self.get_train_val_test_list(
            img_list,
            ratio=self.val_ratio,
            have_test=self.have_test,
            test_ratio=self.test_ratio,
        )
        train_list, val_list, test_list = split_list

        train_anno = self.generate_json(train_list, self.train_dir)
        self.write_json(self.anno_dir / "instances_train2017.json", train_anno)

        val_anno = self.generate_json(val_list, self.val_dir)
        self.write_json(self.anno_dir / "instances_val2017.json", val_anno)

        if test_list:
            test_anno = self.generate_json(test_list, self.test_dir)
            self.write_json(self.anno_dir / "instances_test2017.json", test_anno)
        print(f"Successfully convert, detail in {self.save_dir}")

    def get_img_list(self):
        all_list = self.data_dir.glob("*.*")
        img_list = [v for v in all_list if v.suffix != ".json"]
        return img_list

    def gen_image_label_dir(self, img_list):
        new_image_list = []
        for img_path in tqdm(img_list):
            right_label_path = img_path.with_name(f"{img_path.stem}.json")
            if right_label_path.exists() and self.read_json(str(right_label_path)):
                new_image_list.append(img_path)
        return new_image_list

    def get_train_val_test_list(
        self, img_list, ratio=0.2, have_test=True, test_ratio=0.2
    ):
        random.shuffle(img_list)
        len_img = len(img_list)
        if have_test:
            split_idx_first = int(len_img * ratio)
            split_idx_second = int(len_img * (ratio + test_ratio))

            val_list = img_list[:split_idx_first]
            train_list = img_list[split_idx_second:]
            test_list = img_list[split_idx_first:split_idx_second]
        else:
            split_node = int(len_img * ratio)

            val_list = img_list[:split_node]
            train_list = img_list[split_node:]
            test_list = None
        return train_list, val_list, test_list

    def _init_json(self):
        annotation_info = {
            "type": "instances",
            "info": {
                "year": int(self.cur_year),
                "version": "1.0",
                "description": "For object detection",
                "date_created": self.cur_year,
            },
            "images": [],
            "annotations": [],
            "licenses": [
                {
                    "id": 1,
                    "name": "Apache License v2.0",
                    "url": "https://github.com/RapidAI/LabelConvert/LICENSE",
                }
            ],
            "categories": self.categories,
        }
        return annotation_info

    def _get_category(
        self,
    ):
        json_list = Path(self.data_dir).glob("*.json")
        all_categories = []
        for json_path in json_list:
            json_info = self.read_json(json_path)
            shapes = json_info.get("shapes", [])
            all_categories.extend([v["label"] for v in shapes])

        categories = list(set(all_categories))
        categories.sort(key=all_categories.index)

        coco_categories = []
        for i, cls_name in enumerate(categories):
            coco_categories.append(
                {
                    "supercategory": cls_name,
                    "id": i + 1,
                    "name": cls_name,
                }
            )
        self.cls_to_idx = {v: i + 1 for i, v in enumerate(categories)}
        return coco_categories

    def generate_json(self, img_list, save_dir):
        anno = self._init_json()
        for i, img_path in enumerate(img_list):
            img_id = i + 1

            new_img_name = f"{img_id:012d}{Path(img_path).suffix}"
            new_img_path = save_dir / new_img_name
            self.cp_file(img_path, new_img_path)

            raw_json_path = img_path.with_suffix(".json")
            raw_json_data = self.read_json(raw_json_path)

            img_h = raw_json_data.get("imageHeight")
            img_w = raw_json_data.get("imageWidth")
            img_info = {
                "date_captured": str(self.cur_year),
                "file_name": new_img_name,
                "id": img_id,
                "height": img_h,
                "width": img_w,
            }
            anno["images"].append(img_info)

            shapes = raw_json_data.get("shapes", [])
            anno_list = []
            for shape in shapes:
                shape_type = shape.get("shape_type")
                if shape_type not in [RECTANGLE, POLYGON]:
                    print(
                        f"Current shape type is {shape_type}, not between {RECTANGLE} and {POLYGON}, skip"
                    )
                    continue

                label_name = shape.get("label")
                label_id = self.cls_to_idx[label_name]
                points = np.array(shape.get("points"))

                if shape_type == RECTANGLE:
                    seg_points = [np.ravel(points, order="C").tolist()]

                    x0, y0 = np.min(points, axis=0)
                    x1, y1 = np.max(points, axis=0)
                    w, h = x1 - x1, y1 - y0
                    bbox_points = [x0, y0, w, h]
                    area = w * h

                elif shape_type == POLYGON:
                    seg_points = points.tolist()
                    bbox_points, area = self.cvt_poly_to_rect(img_h, img_w, points)
                else:
                    print(f"Current {shape_type} is not supported!")
                    continue

                one_anno_dict = {
                    "segmentation": seg_points,
                    "area": area,
                    "iscrowd": 0,
                    "image_id": img_id,
                    "bbox": bbox_points,
                    "category_id": label_id,
                    "id": self.object_id,
                }

                anno_list.append(one_anno_dict)
                self.object_id += 1
            anno["annotations"].extend(anno_list)
        return anno

    @staticmethod
    def read_json(json_path: Union[str, Path]):
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def mkdir(dir_path):
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def verify_exists(file_path: Union[Path, str]):
        if not Path(file_path).exists():
            raise FileNotFoundError(f"The {file_path} is not exists!!!")

    @staticmethod
    def write_json(json_path: Union[str, Path], content: dict):
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False)

    def cp_file(self, file_path: Path, dst_dir: Path):
        if not file_path.exists():
            raise FileExistsError(file_path)

        shutil.copy2(str(file_path), dst_dir)

    def cvt_poly_to_rect(self, img_h: int, img_w: int, points):
        mask = np.zeros((img_h, img_w), dtype="uint8")
        img_mask = cv2.fillPoly(mask, np.int32([points]), 255)
        contours, _ = cv2.findContours(img_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contour = contours[0]
        bbox_points = self.get_mini_boxes(contour)
        area = cv2.contourArea(contour)
        return bbox_points, area

    @staticmethod
    def get_mini_boxes(contour) -> List[int]:
        bounding_box = cv2.minAreaRect(contour)
        points = sorted(list(cv2.boxPoints(bounding_box)), key=lambda x: x[0])

        index_1, index_2, index_3, index_4 = 0, 1, 2, 3
        if points[1][1] > points[0][1]:
            index_1 = 0
            index_4 = 1
        else:
            index_1 = 1
            index_4 = 0
        if points[3][1] > points[2][1]:
            index_2 = 2
            index_3 = 3
        else:
            index_2 = 3
            index_3 = 2

        box = [points[index_1], points[index_2], points[index_3], points[index_4]]
        box = np.round(box).astype(np.int32).tolist()
        left_top, right_bottom = box[0], box[2]
        box_w = right_bottom[0] - left_top[0]
        box_h = right_bottom[1] - left_top[1]
        return left_top + [box_w, box_h]


def main():
    parser = argparse.ArgumentParser("Datasets converter from labelme to COCO")
    parser.add_argument(
        "--data_dir",
        type=str,
        default="/Users/joshuawang/projects/_self/LabelConvert/data",
    )
    parser.add_argument("--save_dir", type=str, default=None)
    parser.add_argument("--val_ratio", type=float, default=0.2)
    parser.add_argument("--have_test", action="store_true", default=False)
    parser.add_argument("--test_ratio", type=float, default=0.2)
    args = parser.parse_args()

    converter = LabelmeToCOCO(
        args.data_dir, args.save_dir, args.val_ratio, args.have_test, args.test_ratio
    )
    converter()


if __name__ == "__main__":
    main()
