# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import sys
import tempfile
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent

sys.path.append(str(root_dir))

from label_convert.labelImg_to_yolov5 import LabelImgToYOLOv5

test_file_dir = cur_dir / "test_files"


dataset_name = "labelImg_dataset"


def test_normal():
    with tempfile.TemporaryDirectory() as save_dir:
        save_dir = Path(save_dir)

        data_dir = test_file_dir / dataset_name
        converter = LabelImgToYOLOv5(data_dir, save_dir)
        converter()

        assert save_dir.exists()

        train_data_dir = save_dir / "non_labels"
        assert train_data_dir.exists()

        train_json_path = save_dir / "images"
        assert train_json_path.exists()

        test_data_dir = save_dir / "labels"
        assert test_data_dir.exists()

        test_json_path = save_dir / "classes.txt"
        assert test_json_path.exists()
