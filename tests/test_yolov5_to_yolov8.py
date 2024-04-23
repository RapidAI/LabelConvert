# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import shutil
import sys
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent

sys.path.append(str(root_dir))

from label_convert.yolov5_to_yolov8 import YOLOV5ToYOLOV8

test_file_dir = cur_dir / "test_files"

data_dir_name = "yolov5_dataset"


def test_normal():
    data_dir = test_file_dir / data_dir_name
    converter = YOLOV5ToYOLOV8(data_dir)
    converter()

    save_dir: Path = test_file_dir / f"{data_dir_name}_yolov8"
    assert save_dir.exists()

    train_img_dir = save_dir / "images" / "train"
    assert train_img_dir.exists()

    val_label_dir = save_dir / "labels" / "val"
    assert val_label_dir.exists()

    shutil.rmtree(save_dir)
