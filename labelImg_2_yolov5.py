# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
from pathlib import Path
import shutil
import random


class LabelImgToYOLOV5(object):
    def __init__(self, root_dir, output_dir) -> None:
        self.root_dir = Path(root_dir)
        self.classes_path = self.root_dir / 'classes.txt'

        self.output_dir = Path(output_dir)
        self.out_img_dir = self.output_dir / 'images'
        self.out_label_dir = self.output_dir / 'labels'
        self.out_non_label_dir = self.output_dir / 'non_labels'

        # TODO: 更改图像格式，webp→jpg
        # TODO: 重命名文件

    def __call__(self):
        img_list = self.get_img_list()
        img_list = self.gen_image_label_dir(img_list)

        train_list, val_list, test_list = self.get_train_val_test_list(img_list,
                                                                       ratio=0.2)
        self.write_txt(self.output_dir / 'train.txt', train_list)
        self.write_txt(self.output_dir / 'val.txt', val_list)
        if test_list:
            self.write_txt(self.output_dir / 'test.txt', test_list)

        self.cp_file(self.classes_path, dst_dir=self.output_dir)

    def get_img_list(self):
        img_list = []
        all_list = self.root_dir.glob('*.*')
        for one in all_list:
            cur_suffix = one.suffix
            if cur_suffix != '.txt':
                img_list.append(one)
        return img_list

    def gen_image_label_dir(self, img_list):
        new_image_list = []
        for img_path in img_list:
            right_label_path = img_path.with_name(f'{img_path.stem}.txt')
            if right_label_path.exists():
                self.cp_file(img_path, dst_dir=self.out_img_dir)
                self.cp_file(right_label_path, dst_dir=self.out_label_dir)

                new_image_list.append(img_path)
            else:
                self.cp_file(img_path, dst_dir=self.out_non_label_dir)
        return new_image_list

    def get_train_val_test_list(self, img_list, ratio=0.2,
                                have_test=True, test_ratio=0.2):
        random.shuffle(img_list)
        img_list = [f'{self.out_img_dir / img_path.name}'
                    for img_path in img_list]
        if have_test:
            len_img = len(img_list)
            split_idx_first = int(len_img * ratio)
            split_idx_second = int(len_img * (ratio + test_ratio))

            val_list = img_list[:split_idx_first]
            test_list = img_list[split_idx_first:split_idx_second]
            train_list = img_list[split_idx_second:]
            return train_list, val_list, test_list
        else:
            split_node = int(len(img_list) * ratio)
            val_list = img_list[:split_node]
            train_list = img_list[split_node:]
            return train_list, val_list, None

    @staticmethod
    def mkdir(dir_path):
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def read_txt(txt_path: str) -> list:
        with open(txt_path, 'r', encoding='utf-8') as f:
            data = list(map(lambda x: x.rstrip('\n'), f))
        return data

    @staticmethod
    def write_txt(save_path: str, content: list, mode='w'):
        if isinstance(content, str):
            content = [content]
        with open(save_path, mode, encoding='utf-8') as f:
            for value in content:
                f.write(f'{value}\n')

    def cp_file(self, file_path: Path, dst_dir: Path):
        if not file_path.exists():
            return FileExistsError(file_path)

        if not dst_dir.exists():
            self.mkdir(dst_dir)

        dst_file_path = dst_dir / file_path.name
        shutil.copy2(str(file_path), str(dst_file_path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_dir', type=str)
    parser.add_argument('--out_dir', type=str)
    args = parser.parse_args()

    converter = LabelImgToYOLOV5(args.src_dir, args.out_dir)
    converter()
    print(f'Successfully output to the {args.out_dir}')
