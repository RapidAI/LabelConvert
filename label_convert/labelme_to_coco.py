# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import json
import random
import shutil
import time
import warnings
from pathlib import Path
from typing import List, Optional, Union

import cv2
from tqdm import tqdm


class LabelmeToCOCO:
    def __init__(
        self,
        data_dir: str,
        out_dir: Optional[str] = None,
        val_ratio: float = 0.2,
        have_test: bool = False,
        test_ratio: float = 0.2,
    ):
        self.raw_data_dir = Path(data_dir)
        self.val_ratio = val_ratio
        self.test_ratio = test_ratio
        self.have_test = have_test

        self.verify_exists(self.raw_data_dir)

        if out_dir is None:
            save_dir_name = f"{Path(self.raw_data_dir).name}_COCO_format"
            self.output_dir = self.raw_data_dir.parent / save_dir_name
        self.output_dir = Path(out_dir)
        self.mkdir(self.output_dir)

        self.anno_dir = self.output_dir / "annotations"
        self.mkdir(self.anno_dir)

        self.train_dir = self.output_dir / "train2017"
        self.mkdir(self.train_dir)

        self.val_dir = self.output_dir / "val2017"
        self.mkdir(self.val_dir)

        self.test_dir = None
        if have_test:
            self.test_dir = self.output_dir / "test2017"
            self.mkdir(self.test_dir)

        self.cur_year = time.strftime("%Y", time.localtime(time.time()))

    def __call__(self, mode_list: List[str] = None):
        img_list = self.get_img_list()
        if not img_list:
            raise ValueError(f"{self.raw_data_dir} is empty!")

        img_list = self.gen_image_label_dir(img_list)
        split_list = self.get_train_val_test_list(
            img_list,
            ratio=self.val_ratio,
            have_test=self.have_test,
            test_ratio=self.test_ratio,
        )
        train_list, val_list, test_list = split_list

        # 遍历所有的json，得到所有类别字段
        # TODO

        anno = self._init_json()
        for i, img_path in enumerate(train_list):
            img_id = i + 1

            new_img_name = f"{img_id:012d}.jpg"
            new_img_path = self.train_dir / new_img_name

            # 将图像复制到指定目录下
            self.cp_file(img_path, new_img_path)

            raw_json_path = img_path.with_suffix(".json")
            raw_json_data = self.read_json(raw_json_path)

            # 写入到json中
            img_info = {
                "date_captured": str(self.cur_year),
                "file_name": new_img_name,
                "id": img_id,
                "height": raw_json_data.get("imageHeight"),
                "width": raw_json_data.get("imageWidth"),
            }

            # 记录类别

        print("ok")

        for mode in mode_list:
            # Create the directory of saving the new image.
            save_img_dir = self.output_dir / f"{mode}2017"
            self.mkdir(save_img_dir)

            # Generate json file.
            anno_dir = self.output_dir / "annotations"
            self.mkdir(anno_dir)

            save_json_path = anno_dir / f"instances_{mode}2017.json"
            json_data = self.convert(img_list, save_img_dir, mode)

            self.write_json(save_json_path, json_data)
        print(f"Successfully convert, detail in {self.output_dir}")

    def get_img_list(self):
        all_list = self.raw_data_dir.glob("*.*")
        img_list = [v for v in all_list if v.suffix != ".json"]
        return img_list

    def gen_image_label_dir(self, img_list):
        new_image_list = []
        for img_path in tqdm(img_list):
            right_label_path = img_path.with_name(f"{img_path.stem}.json")
            if right_label_path.exists() and self.read_txt(str(right_label_path)):
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
            "categories": [],
        }
        return annotation_info

    def _get_category(
        self,
    ):
        # 这个放在扫描全部json的中获取
        class_list = self.read_txt(classes_path)
        categories = []
        for i, category in enumerate(class_list, 1):
            categories.append(
                {
                    "supercategory": category,
                    "id": i,
                    "name": category,
                }
            )
        return categories

    def convert(self, img_list, save_img_dir, mode):
        images, annotations = [], []
        for img_id, img_path in enumerate(tqdm(img_list, desc=mode), 1):
            image_dict = self.get_image_info(img_path, img_id, save_img_dir)
            images.append(image_dict)

            label_path = self.raw_data_dir / "labels" / f"{Path(img_path).stem}.txt"
            annotation = self.get_annotation(
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
        if self.raw_data_dir.as_posix() not in img_path.as_posix():
            # relative path (relative to the raw_data_dir)
            # e.g. images/images(3).jpg
            img_path = self.raw_data_dir / img_path

        self.verify_exists(img_path)

        new_img_name = f"{img_id:012d}.jpg"
        save_img_path = save_img_dir / new_img_name
        img_src = cv2.imread(str(img_path))
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

    def get_annotation(self, label_path: Path, img_id, height, width):
        def get_box_info(vertex_info, height, width):
            cx, cy, w, h = [float(i) for i in vertex_info]

            cx = cx * width
            cy = cy * height
            box_w = w * width
            box_h = h * height

            # left top
            x0 = max(cx - box_w / 2, 0)
            y0 = max(cy - box_h / 2, 0)

            # right bottom
            x1 = min(x0 + box_w, width)
            y1 = min(y0 + box_h, height)

            segmentation = [[x0, y0, x1, y0, x1, y1, x0, y1]]
            bbox = [x0, y0, box_w, box_h]
            area = box_w * box_h
            return segmentation, bbox, area

        if not label_path.exists():
            annotation = [
                {
                    "segmentation": [],
                    "area": 0,
                    "iscrowd": 0,
                    "image_id": img_id,
                    "bbox": [],
                    "category_id": -1,
                    "id": self.annotation_id,
                }
            ]
            self.annotation_id += 1
            return annotation

        annotation = []
        label_list = self.read_txt(str(label_path))
        for i, one_line in enumerate(label_list):
            label_info = one_line.split(" ")
            if len(label_info) < 5:
                warnings.warn(f"The {i+1} line of the {label_path} has been corrupted.")
                continue

            category_id, vertex_info = label_info[0], label_info[1:]
            segmentation, bbox, area = get_box_info(vertex_info, height, width)
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
    def read_txt(txt_path):
        with open(str(txt_path), "r", encoding="utf-8") as f:
            data = list(map(lambda x: x.rstrip("\n"), f))
        return data

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
    def write_json(json_path, content: dict):
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False)

    def cp_file(self, file_path: Path, dst_dir: Path):
        if not file_path.exists():
            raise FileExistsError(file_path)

        shutil.copy2(str(file_path), dst_dir)


def main():
    parser = argparse.ArgumentParser("Datasets converter from YOLOV5 to COCO")
    parser.add_argument("--src_dir", type=str)
    parser.add_argument("--out_dir", type=str)
    parser.add_argument("--val_ratio", type=float, default=0.2)
    parser.add_argument("--have_test", action="store_true", default=False)
    parser.add_argument("--test_ratio", type=float, default=0.2)
    args = parser.parse_args()

    converter = LabelmeToCOCO(
        args.src_dir, args.out_dir, args.val_ratio, args.have_test, args.test_ratio
    )
    converter(mode_list=args.mode_list.split(","))


if __name__ == "__main__":
    main()
