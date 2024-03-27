# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import json
import shutil
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

import numpy as np
from tqdm import tqdm

ValueType = Union[str, Path, None]


class COCOTolabelImg:
    def __init__(self, data_dir: ValueType = None, save_dir: ValueType = None):
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
            image_info = id_img_dict.get(one_anno["image_id"])
            img_name = image_info.get("file_name")
            img_height = image_info.get("height")
            img_width = image_info.get("width")

            seg_info = one_anno.get("segmentation")
            if seg_info:
                bbox = self.get_bbox(seg_info)
                xywh = self.xyxy_to_xywh(bbox, img_width, img_height)
                category_id = int(one_anno.get("category_id")) - 1
                xywh_str = " ".join([str(v) for v in xywh])
                label_str = f"{category_id} {xywh_str}"

                # 写入标注的txt文件
                txt_full_path = save_dir / f"{Path(img_name).stem}.txt"
                self.write_txt(txt_full_path, label_str, mode="a")

            # 复制图像到转换后目录
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

    def get_bbox(self, seg_info: List[List[float]]) -> List[float]:
        seg_info = np.array(seg_info[0]).reshape(4, 2)
        x0, y0 = np.min(seg_info, axis=0)
        x1, y1 = np.max(seg_info, axis=0)
        bbox = [x0, y0, x1, y1]
        return bbox

    @staticmethod
    def write_txt(save_path: str, content: List[str], mode="w") -> None:
        if not isinstance(save_path, str):
            save_path = str(save_path)

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
