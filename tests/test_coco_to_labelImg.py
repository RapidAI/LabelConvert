# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import shutil
import sys
import tempfile
from pathlib import Path
from time import sleep

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent

sys.path.append(str(root_dir))

from label_convert.coco_to_labelImg import COCOTolabelImg

test_file_dir = cur_dir / "test_files"

data_dir_name = "COCO_dataset"


def test_normal():
    with tempfile.TemporaryDirectory() as save_dir:
        save_dir = Path(save_dir)
        data_dir = test_file_dir / data_dir_name
        converter = COCOTolabelImg(data_dir, save_dir)
        converter()

        sleep(2)

        assert save_dir.exists()

        train_dir: Path = save_dir / "train"
        assert train_dir.exists()

        val_dir: Path = save_dir / "val"
        assert val_dir.exists()

        shutil.rmtree(save_dir)
