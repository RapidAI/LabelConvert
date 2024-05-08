# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import json
import random
from pathlib import Path
from typing import List, Tuple

import cv2
import numpy as np


class VisCOCO:
    def __init__(
        self,
    ):
        self.font_size = 0.7

    def __call__(self, img_id: int, json_path: str, img_path: str):
        anno_dict = self.read_json(json_path)
        anno_imgs = anno_dict.get("images", None)
        if anno_imgs is None:
            raise ValueError(f"The images of {json_path} cannot be empty.")

        print(f"The anno_dict num_key is: {len(anno_dict)}")
        print(f"The anno_dict key is: {anno_dict.keys()}")
        print(f"The anno_dict num_images is: {len(anno_imgs)}")

        categories = anno_dict["categories"]
        categories_dict = {c["id"]: c["name"] for c in categories}

        class_nums = len(categories_dict.keys())
        color = self.get_class_color(class_nums)

        img_info = anno_dict["images"][img_id - 1]

        img_name = img_info.get("file_name")
        img_full_path = Path(img_path) / img_name
        image = cv2.imread(str(img_full_path))

        annotations = anno_dict["annotations"]
        num_bbox = 0
        img_id = img_info.get("id")
        for anno in annotations:
            if anno["image_id"] != img_id:
                continue

            num_bbox += 1

            class_id = anno["category_id"]
            class_name = categories_dict[class_id]
            class_color = color[class_id - 1]

            segs = anno.get("segmentation", None)
            if segs is not None:
                self.plot_segmentations(image, segs, class_color)
                self.plot_text(image, segs[0][:2], class_color, class_name)

            bbox = anno.get("bbox", None)
            if bbox is None:
                continue

            self.plot_rectangle(image, bbox, class_color)
            self.plot_text(image, bbox, class_color, class_name)

        print(f"The unm_bbox of the display image is: {num_bbox}")
        save_path = f"vis_{Path(img_name).stem}.jpg"
        cv2.imwrite(save_path, image)
        print(f"The {save_path} has been saved the current director.")

    @staticmethod
    def read_json(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def get_class_color(class_nums: int) -> List[Tuple[int]]:
        def random_color():
            return random.randint(0, 255)

        color = [
            (random_color(), random_color(), random_color()) for _ in range(class_nums)
        ]
        return color

    @staticmethod
    def plot_segmentations(
        image: np.ndarray, segs: List[List[float]], class_color: Tuple[int]
    ):
        segs = np.array(segs).reshape(-1, 2)
        cv2.polylines(image, np.int32([segs]), 2, class_color)

    @staticmethod
    def plot_rectangle(
        image: np.ndarray,
        bbox: List[float],
        class_color: Tuple[int],
        thickness: int = 1,
    ):
        x, y, w, h = [round(v) for v in bbox]
        start_point = (int(x), int(y))
        end_point = (int(x + w), int(y + h))
        cv2.rectangle(image, start_point, end_point, class_color, thickness)

    def plot_text(
        self,
        image: np.ndarray,
        bbox: Tuple[float],
        class_color: str,
        class_name: str,
    ):
        txt_size = cv2.getTextSize(
            class_name, cv2.FONT_HERSHEY_SIMPLEX, self.font_size, 1
        )[0]

        x, y = [round(v) for v in bbox[:2]]
        start_point = (x, y + 1)
        end_point = (x + txt_size[0] + 5, y - int(1.5 * txt_size[1]))
        cv2.rectangle(image, start_point, end_point, class_color, -1)

        cv2.putText(
            image,
            class_name,
            (x + 5, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            self.font_size,
            (255, 255, 255),
            1,
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--img_id", type=int, default=1, help="visual which one")
    parser.add_argument(
        "--json_path",
        type=str,
        default="tests/test_files/yolov5_dataset_coco/annotations/instances_train2017.json",
    )
    parser.add_argument(
        "--img_dir", type=str, default="tests/test_files/yolov5_dataset_coco/train2017"
    )
    args = parser.parse_args()

    viser = VisCOCO()
    viser(args.img_id, args.json_path, args.img_dir)


if __name__ == "__main__":
    main()
