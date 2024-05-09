# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import json
import shutil
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

import cv2
import numpy as np
from tqdm import tqdm

ValueType = Union[str, Path, None]


class COCOTolabelImg:
    def __init__(self, data_dir: ValueType = None, save_dir: ValueType = None):
        if data_dir is None:
            raise ValueError("data_dir must not be None")

        self.data_dir = Path(data_dir)
        self.verify_exists(self.data_dir)

        anno_dir = self.data_dir / "annotations"
        self.verify_exists(anno_dir)

        self.train_json = anno_dir / "instances_train2017.json"
        self.val_json = anno_dir / "instances_val2017.json"
        self.verify_exists(self.train_json)
        self.verify_exists(self.val_json)

        self.train2017_dir = self.data_dir / "train2017"
        self.val2017_dir = self.data_dir / "val2017"
        self.verify_exists(self.train2017_dir)
        self.verify_exists(self.val2017_dir)

        if save_dir is None:
            save_dir = self.data_dir.parent / f"{self.data_dir.name}_labelImg"
        self.save_dir = Path(save_dir)
        self.mkdir(self.save_dir)

        self.save_train_dir = self.save_dir / "train"
        self.mkdir(self.save_train_dir)

        self.save_val_dir = self.save_dir / "val"
        self.mkdir(self.save_val_dir)

    def __call__(
        self,
    ) -> None:
        train_list = [self.train_json, self.save_train_dir, self.train2017_dir]
        self.convert(train_list)

        val_list = [self.val_json, self.save_val_dir, self.val2017_dir]
        self.convert(val_list)

        print(f"Successfully convert, detail in {self.save_dir}")

    def convert(self, info_list: List[Path]) -> None:
        json_path, save_dir, img_dir = info_list

        data = self.read_json(str(json_path))
        self.gen_classes_txt(save_dir, data.get("categories"))

        id_img_dict = {v["id"]: v for v in data.get("images")}
        all_annotaions = data.get("annotations")
        for one_anno in tqdm(all_annotaions):
            img_info = id_img_dict.get(one_anno["image_id"])
            img_name = img_info.get("file_name")
            img_height = img_info.get("height")
            img_width = img_info.get("width")
            category_id = int(one_anno.get("category_id")) - 1

            bbox_info = one_anno.get("bbox", None)
            seg_info = one_anno.get("segmentation", None)

            if bbox_info:
                x0, y0, w, h = bbox_info
                xyxy_bbox = [x0, y0, x0 + w, y0 + h]
                xywh = self.xyxy_to_xywh(xyxy_bbox, img_width, img_height)
            elif seg_info:
                points = np.array(seg_info).reshape(4, 2)
                bbox = self.get_bbox_from_poly(img_height, img_width, points)
                xywh = self.xyxy_to_xywh(bbox, img_width, img_height)
            else:
                print("The bbox and segmentation are all None, skip current anno.")
                continue

            xywh_str = " ".join([str(v) for v in xywh])
            label_str = f"{category_id} {xywh_str}"

            txt_full_path = save_dir / f"{Path(img_name).stem}.txt"
            self.write_txt(txt_full_path, label_str, mode="a")

            img_full_path = img_dir / img_name
            shutil.copy2(img_full_path, save_dir)

    @staticmethod
    def read_json(json_path: Union[Path, str]) -> Dict[str, Any]:
        with open(str(json_path), "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def gen_classes_txt(self, save_dir: Path, categories_dict: List[Dict[str, str]]):
        class_info = [value["name"] for value in categories_dict]
        self.write_txt(save_dir / "classes.txt", class_info)

    def get_bbox_from_poly(
        self, img_h: int, img_w: int, points: np.ndarray
    ) -> List[float]:
        mask = np.zeros((img_h, img_w), dtype="uint8")
        img_mask = cv2.fillPoly(mask, np.int32([points]), 255)
        contours, _ = cv2.findContours(img_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contour = contours[0]
        bbox = self.get_mini_boxes(contour)
        return bbox

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
        return left_top + right_bottom

    @staticmethod
    def write_txt(save_path: str, content: List[str], mode="w") -> None:
        if isinstance(content, str):
            content = [content]

        with open(save_path, mode, encoding="utf-8") as f:
            for value in content:
                f.write(f"{value}\n")

    @staticmethod
    def xyxy_to_xywh(
        xyxy: List[float], img_width: int, img_height: int
    ) -> Tuple[float, float, float, float]:
        """
        xyxy: (List[float]), [x1, y1, x2, y2]
        """
        x_center = (xyxy[0] + xyxy[2]) / (2 * img_width)
        y_center = (xyxy[1] + xyxy[3]) / (2 * img_height)

        box_w = abs(xyxy[2] - xyxy[0])
        box_h = abs(xyxy[3] - xyxy[1])

        w = box_w / img_width
        h = box_h / img_height
        return x_center, y_center, w, h

    @staticmethod
    def verify_exists(file_path: Union[str, Path]) -> None:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"The {file_path} is not exists!!!")

    @staticmethod
    def mkdir(dir_path: Union[str, Path]):
        Path(dir_path).mkdir(parents=True, exist_ok=True)


def main():
    parser = argparse.ArgumentParser("Datasets convert from COCO to labelImg")
    parser.add_argument(
        "--data_dir",
        type=str,
        default=None,
        help="Dataset root path",
    )
    parser.add_argument(
        "--save_dir", type=str, default=None, help="Path to save the converted dataset."
    )
    args = parser.parse_args()

    converter = COCOTolabelImg(args.data_dir, args.save_dir)
    converter()


if __name__ == "__main__":
    main()
