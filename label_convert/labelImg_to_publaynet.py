# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import shutil
import json
import random
from pathlib import Path
from typing import List, Union, Dict

import cv2
from tqdm import tqdm


class LabelImgToPubLayNet:
    def __init__(
        self, val_ratio: float = 0.2, have_test: bool = True, test_ratio: float = 0.2
    ):
        self.val_ratio = val_ratio

        self.have_test = have_test
        self.test_ratio = test_ratio

    def __call__(self, data_dir: Union[Path, str]):
        cls_path = Path(data_dir) / "classes.txt"
        cls_info = self.read_txt(cls_path)

        train_list, val_list, test_list = self.get_train_val_test_list(data_dir)

        # 新建目录，放置train val test下图像和对应txt
        new_data_dir = Path(data_dir).with_name(f'{Path(data_dir).stem}_publaynet')
        train_data_dir = new_data_dir / 'train'
        val_data_dir = new_data_dir / 'val'
        test_data_dir = new_data_dir / 'test'
        self.mkdir(new_data_dir)

        json_path = Path(data_dir).with_name(f'{Path(data_dir).stem}.json')
        self.gen_json(train_list, cls_info, json_path)
        self.gen_json(val_list, cls_info, json_path)

        if test_list:
            self.gen_json(test_list, cls_info, json_path)

    def cp_file(self, file_path: Path, dst_dir: Path):
        if not file_path.exists():
            raise FileExistsError(file_path)

        if not dst_dir.exists():
            self.mkdir(dst_dir)

        dst_file_path = dst_dir / file_path.name
        shutil.copy2(str(file_path), str(dst_file_path))

    def get_train_val_test_list(self,  data_dir: Union[Path, str]):
        img_list = [p for p in data_dir.iterdir() if p.suffix != ".txt"]
        random.shuffle(img_list)

        len_img = len(img_list)
        if self.have_test:
            split_idx_first = int(len_img * self.val_ratio)
            split_idx_second = int(len_img * (self.val_ratio + self.test_ratio))

            val_list = img_list[:split_idx_first]
            train_list = img_list[split_idx_second:]
            test_list = img_list[split_idx_first:split_idx_second]
        else:
            split_node = int(len_img * self.val_ratio)

            val_list = img_list[:split_node]
            train_list = img_list[split_node:]
            test_list = None
        return train_list, val_list, test_list

    def gen_json(self, img_list: List[Union[Path, str]], cls_info: List[str],
                 json_path: Union[Path, str]):
        res = self.new_res_json()
        res = self.gen_categories(res, cls_info)

        for image_id, img_path in enumerate(tqdm(img_list)):
            img = cv2.imread(str(img_path))
            img_h, img_w = img.shape[:2]

            one_dict = {
                "file_name": img_path.name,
                "width": img_w,
                "height": img_h,
                "id": image_id,
            }

            res["images"].append(one_dict)

            label_path = img_path.with_name(f"{img_path.stem}.txt")
            try:
                label_datas = self.read_txt(label_path)
            except:
                print(f"{label_path} meets error.")
                continue

            for label_id, label_data in enumerate(label_datas):
                cls_idx, x, y, w, h = label_data.split(" ")

                left_x, left_y, box_w, box_h = self.xywh_to_xyxy(
                    float(x), float(y), float(w), float(h), img_h=img_h, img_w=img_w
                )

                anno_dict = {
                    "segmentation": [[left_x, left_y, box_w, box_h]],
                    "area": box_w * box_h,
                    "iscrowd": 0,
                    "image_id": image_id,
                    "bbox": [left_x, left_y, box_w, box_h],
                    "category_id": int(cls_idx) + 1,
                    "id": label_id,
                }
                res["annotations"].append(anno_dict)

        self.save_json(json_path, res)

    def new_res_json(self, ) -> Dict[str, List]:
        return {"images": [], "annotations": [], "categories": []}

    def gen_categories(self, res: Dict[str, List[]], cls_info: List[str]):
        res["categories"] = [
            {"supercategory": "", "id": i + 1, "name": cls_name}
            for i, cls_name in enumerate(cls_info)
        ]
        return res

    def save_json(self, json_path: Union[Path, str], content):
        with open(str(json_path), "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False)

    @staticmethod
    def read_txt(txt_path: Union[Path, str]) -> List[str]:
        with open(txt_path, "r", encoding="utf-8") as f:
            data = [v.rstrip("\n") for v in f]
        return data

    @staticmethod
    def xywh_to_xyxy(
        x_center: Union[float, int],
        y_center: Union[float, int],
        w: Union[float, int],
        h: Union[float, int],
        img_w: int,
        img_h: int,
    ) -> tuple([float, float, float, float]):
        real_x_center = x_center * img_w
        real_y_center = y_center * img_h
        real_box_w = w * img_w
        real_box_h = h * img_h
        x0 = real_x_center - (real_box_w / 2)
        y0 = real_y_center - (real_box_h / 2)
        return x0, y0, real_box_w, real_box_h

    @staticmethod
    def mkdir(dir_path):
        Path(dir_path).mkdir(parents=True, exist_ok=True)


def main():
    pass


if __name__ == '__main__':
    main()