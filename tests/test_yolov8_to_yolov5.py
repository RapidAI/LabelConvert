# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import sys
import tempfile
from pathlib import Path
from time import sleep

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent

sys.path.append(str(root_dir))

from label_convert.yolov8_to_yolov5 import YOLOv8ToYOLOv5

test_file_dir = cur_dir / "test_files"

data_dir_name = "yolov8_dataset"


def test_normal():
    with tempfile.TemporaryDirectory() as save_dir:
        save_dir = Path(save_dir)
        data_dir = test_file_dir / data_dir_name
        converter = YOLOv8ToYOLOv5(data_dir, save_dir)
        converter()

        sleep(2)

        assert save_dir.exists()

        train_img_dir = save_dir / "images"
        assert train_img_dir.exists()

        val_label_dir = save_dir / "labels"
        assert val_label_dir.exists()

        train_txt_path = save_dir / "train.txt"
        assert train_txt_path.exists()

        classes_txt_path = save_dir / "classes.txt"
        assert classes_txt_path.exists()
