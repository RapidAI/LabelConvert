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


dataset_name = "labelImg_dataset"


def test_normal():
    data_dir = test_file_dir / dataset_name
    convert = LabelImgToPubLayNet(data_dir=data_dir)
    convert()

    save_dir = test_file_dir / f"{dataset_name}_publaynet"

    train_data_dir = save_dir / "train"
    assert train_data_dir.exists()

    train_json_path = save_dir / "train.json"
    assert train_json_path.exists()

    test_data_dir = save_dir / "test"
    assert test_data_dir.exists()

    test_json_path = save_dir / "test.json"
    assert test_json_path.exists()

    shutil.rmtree(save_dir)
