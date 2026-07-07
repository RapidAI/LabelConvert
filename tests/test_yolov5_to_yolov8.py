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

from label_convert.yolov5_to_yolov8 import YOLOv5ToYOLOv8

test_file_dir = cur_dir / "test_files"

data_dir_name = "yolov5_dataset"


def test_normal():
    with tempfile.TemporaryDirectory() as save_dir:
        save_dir = Path(save_dir)
        data_dir = test_file_dir / data_dir_name
        converter = YOLOv5ToYOLOv8(data_dir, save_dir)
        converter()

        sleep(2)

        assert save_dir.exists()

        train_img_dir = save_dir / "images" / "train"
        assert train_img_dir.exists()

        val_label_dir = save_dir / "labels" / "val"
        assert val_label_dir.exists()
