# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import shutil
from pathlib import Path
from typing import List, Tuple, Union

import yaml
from tqdm import tqdm

ValueType = Union[str, Path, None]


class YOLOv8ToYOLOv5:
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
            save_dir = self.data_dir.parent / f"{Path(self.data_dir).name}_yolov5"
        self.save_dir = save_dir
        self.mkdir(self.save_dir)

        self.yaml_path = yaml_path

        self.save_img_dir = save_dir / "images"
        self.mkdir(self.save_img_dir)

        self.save_label_dir = save_dir / "labels"
        self.mkdir(self.save_label_dir)

    def __call__(self, mode_list: Tuple[str] = ("train", "val")):
        if not mode_list:
            raise ValueError("mode_list is empty!!")

        for mode in tqdm(mode_list):
            img_dir = self.img_dir / mode
            img_list = list(img_dir.iterdir())

            img_relative_list = []
            # copy images to new img dir
            for img_path in img_list:
                shutil.copy(img_path, self.save_img_dir)

                label_path = self.label_dir / mode / img_path.with_suffix(".txt").name
                shutil.copy(label_path, self.save_label_dir)

                new_img_path = Path("images") / img_path.name
                img_relative_list.append(new_img_path)

            txt_path = self.save_dir / f"{mode}.txt"
            self.write_txt(txt_path, img_relative_list)

        class_txt_path = self.save_dir / "classes.txt"
        class_content = ""
        if self.yaml_path is not None:
            yaml_data = self.read_yaml(self.yaml_path)
            class_content = list(yaml_data["names"].values())
        self.write_txt(class_txt_path, class_content)
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
    def read_yaml(yaml_path):
        with open(yaml_path, "rb") as f:
            data = yaml.load(f, Loader=yaml.Loader)
        return data


def main():
    parser = argparse.ArgumentParser("Datasets converter from YOLOv8 to YOLOv5")
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
    parser.add_argument("--yaml_path", type=str, default=None)
    args = parser.parse_args()

    converter = YOLOv8ToYOLOv5(args.data_dir, args.save_dir, args.yaml_path)
    converter(mode_list=args.mode_list.split(","))


if __name__ == "__main__":
    main()
