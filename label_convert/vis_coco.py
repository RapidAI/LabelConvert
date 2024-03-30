# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import json
import platform
import random
from pathlib import Path

import cv2
import numpy as np


class VisCOCO:
    def __init__(
        self,
    ):
        self.font_size = 0.7

    def __call__(self, img_id: int, json_path, img_path):
        with open(json_path, "r", encoding="utf-8") as annos:
            anno_dict = json.load(annos)

        anno_imgs = anno_dict.get("images", None)
        if anno_imgs is None:
            raise ValueError(f"The images of {json_path} cannot be empty.")

        print("The anno_dict num_key is:", len(anno_dict))
        print("The anno_dict key is:", anno_dict.keys())
        print("The anno_dict num_images is:", len(anno_imgs))

        categories = anno_dict["categories"]
        categories_dict = {c["id"]: c["name"] for c in categories}

        class_nums = len(categories_dict.keys())
        color = [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(class_nums)
        ]

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

            # plot sgmentations
            segs = anno.get("segmentation", None)
            if segs is not None:
                segs = np.array(segs).reshape(-1, 2)
                cv2.polylines(image, np.int32([segs]), 2, class_color)

            # plot rectangle
            x, y, w, h = [round(v) for v in anno["bbox"]]
            cv2.rectangle(
                image, (int(x), int(y)), (int(x + w), int(y + h)), class_color, 2
            )

            txt_size = cv2.getTextSize(
                class_name, cv2.FONT_HERSHEY_SIMPLEX, self.font_size, 1
            )[0]
            cv2.rectangle(
                image,
                (x, y + 1),
                (x + txt_size[0] + 5, y - int(1.5 * txt_size[1])),
                class_color,
                -1,
            )
            cv2.putText(
                image,
                class_name,
                (x + 5, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                self.font_size,
                (255, 255, 255),
                1,
            )

        print("The unm_bbox of the display image is:", num_bbox)

        cur_os = platform.system()
        if cur_os == "Windows":
            cv2.namedWindow(img_name, 0)
            cv2.resizeWindow(img_name, 1000, 1000)
            cv2.imshow(img_name, image)
            cv2.waitKey(0)
        else:
            save_path = f"vis_{Path(img_name).stem}.jpg"
            cv2.imwrite(save_path, image)
            print(f"The {save_path} has been saved the current director.")


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
