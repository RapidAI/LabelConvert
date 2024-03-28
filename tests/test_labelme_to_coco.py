# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import shutil
import sys
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent

sys.path.append(str(root_dir))

from label_convert.labelme_to_coco import LabelmeToCOCO

test_file_dir = cur_dir / "test_files"

data_dir_name = "labelme_dataset"


def test_normal():
    data_dir = test_file_dir / data_dir_name
    converter = LabelmeToCOCO(data_dir)
    converter()

    save_dir: Path = test_file_dir / f"{data_dir_name}_coco"
    assert save_dir.exists()

    train_json_path = save_dir / "annotations" / "instances_train2017.json"
    assert train_json_path.exists()

    val_json_path = save_dir / "annotations" / "instances_val2017.json"
    assert val_json_path.exists()

    train_dir: Path = save_dir / "train2017"
    assert train_dir.exists()

    val_dir: Path = save_dir / "val2017"
    assert val_dir.exists()

    shutil.rmtree(save_dir)
