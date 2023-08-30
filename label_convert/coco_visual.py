# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import json
import os
import platform
import random

import cv2


class VisCOCO:
    def __init__(
        self,
    ):
        pass

    def __call__(self, num_image, json_path, img_path):
        with open(json_path, "r", encoding="utf-8") as annos:
            annotation_json = json.load(annos)

        print("The annotation_json num_key is:", len(annotation_json))
        print("The annotation_json key is:", annotation_json.keys())
        print("The annotation_json num_images is:", len(annotation_json["images"]))

        categories = annotation_json["categories"]
        categories_dict = {c["id"]: c["name"] for c in categories}
        class_nums = len(categories_dict.keys())
        color = [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(class_nums)
        ]

        image_name = annotation_json["images"][num_image - 1]["file_name"]
        img_id = annotation_json["images"][num_image - 1]["id"]
        image_path = os.path.join(img_path, str(image_name).zfill(5))
        image = cv2.imread(image_path, 1)

        annotations = annotation_json["annotations"]
        num_bbox = 0
        for anno in annotations:
            if anno["image_id"] == img_id:
                num_bbox = num_bbox + 1

                class_id = anno["category_id"]
                class_name = categories_dict[class_id]
                class_color = color[class_id - 1]

                x, y, w, h = list(map(int, anno["bbox"]))
                cv2.rectangle(
                    image, (int(x), int(y)), (int(x + w), int(y + h)), class_color, 2
                )

                font_size = 0.7
                txt_size = cv2.getTextSize(
                    class_name, cv2.FONT_HERSHEY_SIMPLEX, font_size, 1
                )[0]
                cv2.rectangle(
                    image,
                    (x, y + 1),
                    (x + txt_size[0] + 10, y - int(2 * txt_size[1])),
                    class_color,
                    -1,
                )
                cv2.putText(
                    image,
                    class_name,
                    (x + 5, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    font_size,
                    (255, 255, 255),
                    1,
                )

        print("The unm_bbox of the display image is:", num_bbox)

        cur_os = platform.system()
        if cur_os == "Windows":
            cv2.namedWindow(image_name, 0)
            cv2.resizeWindow(image_name, 1000, 1000)
            cv2.imshow(image_name, image)
            cv2.waitKey(0)
        else:
            save_path = f"visul_{num_image}.jpg"
            cv2.imwrite(save_path, image)
            print(f"The {save_path} has been saved the current director.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vis_num", type=int, default=1, help="visual which one")
    parser.add_argument("--json_path", type=str, required=True)
    parser.add_argument("--img_dir", type=str, required=True)
    args = parser.parse_args()

    viser = VisCOCO()
    viser(args.vis_num, args.json_path, args.img_dir)


if __name__ == "__main__":
    main()
