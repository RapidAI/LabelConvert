# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import shutil
import sys
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent

sys.path.append(str(root_dir))

from label_convert.coco_to_labelimg import COCO2labelImg

test_file_dir = cur_dir / "test_files"


def test_normal():
    data_dir = test_file_dir / "YOLOV5_COCO_format"
    converter = COCO2labelImg(data_dir)
    converter()

    save_dir: Path = test_file_dir / "COCO_labelImg_format"
    assert save_dir.exists()

    train_dir: Path = save_dir / "train"
    assert train_dir.exists()

    val_dir: Path = save_dir / "val"
    assert val_dir.exists()

    shutil.rmtree(save_dir)
