# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import shutil
from pathlib import Path
from typing import Tuple, Union

from tqdm import tqdm

ValueType = Union[str, Path, None]


class YOLOv5ToYOLOv8:
    def __init__(self, data_dir: ValueType = None, save_dir: ValueType = None):
        if data_dir is None:
            raise ValueError("data_dir must not be None")
        self.data_dir = Path(data_dir)
        self.verify_exists(self.data_dir)

        self.img_dir = self.data_dir / "images"
        self.verify_exists(self.img_dir)

        self.label_dir = self.data_dir / "labels"
        self.verify_exists(self.label_dir)

        if save_dir is None:
            save_dir = self.data_dir.parent / f"{Path(self.data_dir).name}_yolov8"
        self.save_dir = save_dir
        self.mkdir(self.save_dir)

        self.save_img_dir = save_dir / "images"
        self.mkdir(self.save_img_dir)

        self.save_label_dir = save_dir / "labels"
        self.mkdir(self.save_label_dir)

    def __call__(self, mode_list: Tuple[str] = ("train", "val")):
        if not mode_list:
            raise ValueError("mode_list is empty!!")

        for mode in tqdm(mode_list):
            txt_path = self.data_dir / f"{mode}.txt"
            self.verify_exists(txt_path)
            img_list = self.read_txt(txt_path)

            save_mode_img_dir = self.save_img_dir / mode
            self.mkdir(save_mode_img_dir)

            save_mode_label_dir = self.save_label_dir / mode
            self.mkdir(save_mode_label_dir)

            # copy images to new img dir
            for img_path in img_list:
                img_full_path = self.data_dir / img_path
                shutil.copy(img_full_path, save_mode_img_dir)

                label_path = self.label_dir / Path(img_path).with_suffix(".txt").name
                shutil.copy(label_path, save_mode_label_dir)

        print(f"Successfully convert, detail in {self.save_dir}")

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


def main():
    parser = argparse.ArgumentParser("Datasets converter from YOLOv5 to YOLOv8")
    parser.add_argument(
        "--data_dir",
        type=str,
        default="tests/test_files/yolov5_dataset",
        help="Dataset root path",
    )
    parser.add_argument("--save_dir", type=str, default=None)
    parser.add_argument(
        "--mode_list", type=str, default="train,val", help="generate which mode"
    )
    args = parser.parse_args()

    converter = YOLOv5ToYOLOv8(args.data_dir, args.save_dir)
    converter(mode_list=args.mode_list.split(","))


if __name__ == "__main__":
    main()
