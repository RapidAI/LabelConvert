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

from label_convert.labelImg_to_publaynet import LabelImgToPubLayNet

test_file_dir = cur_dir / "test_files"

dataset_name = "labelImg_dataset"


def test_normal():
    data_dir = test_file_dir / dataset_name

    with tempfile.TemporaryDirectory() as save_dir:
        save_dir = Path(save_dir)
        convert = LabelImgToPubLayNet(data_dir=data_dir, save_dir=save_dir)
        convert()

        sleep(0.5)

        train_data_dir = save_dir / "train"
        assert train_data_dir.exists()

        train_json_path = save_dir / "train.json"
        assert train_json_path.exists()

        test_data_dir = save_dir / "test"
        assert test_data_dir.exists()

        test_json_path = save_dir / "test.json"
        assert test_json_path.exists()
