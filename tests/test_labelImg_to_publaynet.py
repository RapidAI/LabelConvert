# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import shutil
import sys
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent

sys.path.append(str(root_dir))

from label_convert.labelImg_to_publaynet import LabelImgToPubLayNet

test_file_dir = cur_dir / "test_files"

convert = LabelImgToPubLayNet()


def test_normal():
    data_dir = test_file_dir / "labelImg_dataset"

    convert(data_dir)

    new_data_dir = test_file_dir / "labelImg_dataset_publaynet"

    train_data_dir = new_data_dir / "train"
    assert train_data_dir.exists()

    train_json_path = new_data_dir / "train.json"
    assert train_json_path.exists()

    test_data_dir = new_data_dir / "test"
    assert test_data_dir.exists()

    test_json_path = new_data_dir / "test.json"
    assert test_json_path.exists()

    shutil.rmtree(new_data_dir)
