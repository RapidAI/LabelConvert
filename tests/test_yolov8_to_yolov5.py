# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import shutil
import sys
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent

sys.path.append(str(root_dir))

from label_convert.yolov8_to_yolov5 import YOLOv8ToYOLOv5

test_file_dir = cur_dir / "test_files"

data_dir_name = "yolov8_dataset"


def test_normal():
    data_dir = test_file_dir / data_dir_name
    converter = YOLOv8ToYOLOv5(data_dir)
    converter()

    save_dir: Path = test_file_dir / f"{data_dir_name}_yolov5"
    assert save_dir.exists()

    train_img_dir = save_dir / "images"
    assert train_img_dir.exists()

    val_label_dir = save_dir / "labels"
    assert val_label_dir.exists()

    train_txt_path = save_dir / "train.txt"
    assert train_txt_path.exists()

    classes_txt_path = save_dir / "classes.txt"
    assert classes_txt_path.exists()

    shutil.rmtree(save_dir)
