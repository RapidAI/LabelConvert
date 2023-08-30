# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import glob
import json
import os
import shutil
import time
from pathlib import Path

import cv2
import yaml
from tqdm import tqdm


def read_txt(txt_path):
    with open(str(txt_path), "r", encoding="utf-8") as f:
        data = list(map(lambda x: x.rstrip("\n"), f))
    return data


def mkdir(dir_path):
    Path(dir_path).mkdir(parents=True, exist_ok=True)


def verify_exists(file_path):
    file_path = Path(file_path).resolve()
    if not file_path.exists():
        raise FileNotFoundError(f"The {file_path} is not exists!!!")


class YOLOV5CFG2COCO:
    def __init__(self, yaml_path):
        verify_exists(yaml_path)
        with open(yaml_path, "r", encoding="UTF-8") as f:
            self.data_cfg = yaml.safe_load(f)

        self.root_dir = Path(yaml_path).parent.parent
        self.root_data_dir = Path(self.data_cfg.get("path"))

        self.train_path = self._get_data_dir("train")
        self.val_path = self._get_data_dir("val")

        nc = self.data_cfg["nc"]

        if "names" in self.data_cfg:
            self.names = self.data_cfg.get("names")
        else:
            # assign class names if missing
            self.names = [f"class{i}" for i in range(self.data_cfg["nc"])]

        assert (
            len(self.names) == nc
        ), f"{len(self.names)} names found for nc={nc} dataset in {yaml_path}"

        # 构建COCO格式目录
        self.dst = self.root_dir / f"{Path(self.root_data_dir).stem}_COCO_format"
        self.coco_train = "train2017"
        self.coco_val = "val2017"
        self.coco_annotation = "annotations"
        self.coco_train_json = (
            self.dst / self.coco_annotation / f"instances_{self.coco_train}.json"
        )
        self.coco_val_json = (
            self.dst / self.coco_annotation / f"instances_{self.coco_val}.json"
        )

        mkdir(self.dst)
        mkdir(self.dst / self.coco_train)
        mkdir(self.dst / self.coco_val)
        mkdir(self.dst / self.coco_annotation)

        # 构建json内容结构
        self.type = "instances"
        self.categories = []
        self._get_category()
        self.annotation_id = 1

        cur_year = time.strftime("%Y", time.localtime(time.time()))
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
                "url": "https://choosealicense.com/licenses/apache-2.0/",
            }
        ]

    def _get_data_dir(self, mode):
        data_dir = self.data_cfg.get(mode)
        if data_dir:
            if isinstance(data_dir, str):
                full_path = [str(self.root_data_dir / data_dir)]
            elif isinstance(data_dir, list):
                full_path = [str(self.root_data_dir / one_dir) for one_dir in data_dir]
            else:
                raise TypeError(f"{data_dir} is not str or list.")
        else:
            raise ValueError(f"{mode} dir is not in the yaml.")
        return full_path

    def _get_category(self):
        for i, category in enumerate(self.names, start=1):
            self.categories.append(
                {
                    "supercategory": category,
                    "id": i,
                    "name": category,
                }
            )

    def generate(self):
        self.train_files = self.get_files(self.train_path)
        self.valid_files = self.get_files(self.val_path)

        train_dest_dir = Path(self.dst) / self.coco_train
        self.gen_dataset(
            self.train_files, train_dest_dir, self.coco_train_json, mode="train"
        )

        val_dest_dir = Path(self.dst) / self.coco_val
        self.gen_dataset(self.valid_files, val_dest_dir, self.coco_val_json, mode="val")

        print(f"The output directory is: {self.dst}")

    def get_files(self, path):
        IMG_FORMATS = ["bmp", "dng", "jpeg", "jpg", "mpo", "png", "tif", "tiff", "webp"]
        f = []
        for p in path:
            p = Path(p)
            if p.is_dir():
                f += glob.glob(str(p / "**" / "*.*"), recursive=True)
            elif p.is_file():  # file
                with open(p, "r", encoding="utf-8") as t:
                    t = t.read().strip().splitlines()
                    parent = str(p.parent) + os.sep
                    f += [
                        x.replace("./", parent) if x.startswith("./") else x for x in t
                    ]
            else:
                raise FileExistsError(f"{p} does not exist")

        im_files = sorted(
            x.replace("/", os.sep) for x in f if x.split(".")[-1].lower() in IMG_FORMATS
        )
        return im_files

    def gen_dataset(self, img_paths, target_img_path, target_json, mode):
        """
        https://cocodataset.org/#format-data

        """
        images = []
        annotations = []
        sa, sb = (
            os.sep + "images" + os.sep,
            os.sep + "labels" + os.sep,
        )  # /images/, /labels/ substrings

        for img_id, img_path in enumerate(tqdm(img_paths, desc=mode), 1):
            label_path = sb.join(img_path.rsplit(sa, 1)).rsplit(".", 1)[0] + ".txt"

            img_path = Path(img_path)

            verify_exists(img_path)

            imgsrc = cv2.imread(str(img_path))
            height, width = imgsrc.shape[:2]

            dest_file_name = f"{img_id:012d}.jpg"
            save_img_path = target_img_path / dest_file_name

            if img_path.suffix.lower() == ".jpg":
                shutil.copyfile(img_path, save_img_path)
            else:
                cv2.imwrite(str(save_img_path), imgsrc)

            images.append(
                {
                    "date_captured": "2021",
                    "file_name": dest_file_name,
                    "id": img_id,
                    "height": height,
                    "width": width,
                }
            )

            if Path(label_path).exists():
                new_anno = self.read_annotation(label_path, img_id, height, width)
                if len(new_anno) > 0:
                    annotations.extend(new_anno)
                else:
                    raise ValueError(f"{label_path} is empty")
            else:
                raise FileNotFoundError(f"{label_path} not exists")

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

    def read_annotation(self, txt_file, img_id, height, width):
        annotation = []
        all_info = read_txt(txt_file)
        for label_info in all_info:
            # 遍历一张图中不同标注对象
            label_info = label_info.split(" ")
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
                    "category_id": int(category_id) + 1,
                    "id": self.annotation_id,
                }
            )
            self.annotation_id += 1
        return annotation

    @staticmethod
    def _get_annotation(vertex_info, height, width):
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


def main():
    parser = argparse.ArgumentParser("Datasets converter from YOLOV5 to COCO")
    parser.add_argument(
        "--yaml_path",
        type=str,
        default="dataset/YOLOV5_yaml/sample.yaml",
        help="Dataset cfg file",
    )
    args = parser.parse_args()

    converter = YOLOV5CFG2COCO(args.yaml_path)
    converter.generate()


if __name__ == "__main__":
    main()
