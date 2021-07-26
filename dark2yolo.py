import cv2 as cv
from pathlib import Path
import argparse
import json
import configparser as cfg
import os 
import shutil
# pathlib https://www.cnblogs.com/sigai/p/8074329.html
# coco 数据格式 http://www.xyu.ink/3612.html
'''
gendata_path : the path of gen_config.data


classes=2
train=gen_train.txt
valid=gen_valid.txt
names=qmobj.names

'''

class YOLO2COCO:
    def __init__(self,genconfig_data): 
        self.src_data=genconfig_data
        self.src=Path(self.src_data).parent
        self.dst=Path(self.src) / "coco"
        self.coco_train="train2017"
        self.coco_valid="valid2017"
        self.coco_annotation="annotations"
        self.coco_train_json=Path(self.dst)/Path(self.coco_annotation) / f'instances_{self.coco_train}.json'
        self.coco_valid_json=Path(self.dst)/Path(self.coco_annotation) / f'instances_{self.coco_valid}.json'
        self.type = 'instances'
        self.categories = []
        self.info = {
            'year': 2021,
            'version': '1.0',
            'description': 'For object detection',
            'date_created': '2021',
        }
        self.licenses = [{
            'id': 1,
            'name': 'GNU General Public License v3.0',
            'url': 'https://github.com/zhiqwang/yolov5-rt-stack/blob/master/LICENSE',
        }]

        if not Path(self.dst).is_dir():
            Path(self.dst).mkdir()

        if not (Path(self.dst )/ self.coco_train).is_dir():
            ( Path(self.dst)/self.coco_train).mkdir()

        
        if not (Path(self.dst )/ self.coco_valid).is_dir():
            ( Path(self.dst)/self.coco_valid).mkdir()

        
        if not (Path(self.dst )/ self.coco_annotation).is_dir():
            ( Path(self.dst)/self.coco_annotation).mkdir()

        if Path(self.src_data).is_file():
            self.ready=True
            self.initcfg()
        else:
            self.ready=False

    def initcfg(self):
        if  not self.ready:
            return 
        self.cnf = cfg.RawConfigParser()
        with open(self.src_data) as f:
            file_content = '[dummy_section]\n' + f.read()
        self.cnf.read_string(file_content)

    def getint(self,key):
        if not self.ready:
            return 0
        return int(self.cnf.get("dummy_section",key))

    def getstring(self,key):
        if not self.ready:
            return ""
        return self.cnf.get("dummy_section",key)




    def get_path(self,name):
        content=[]
        with open(name) as f:
            allfiles=f.readlines()
        for file in allfiles:
            if not os.path.isabs(file):
                this_path=Path(self.src)/file.strip()
                content.append(str(this_path))
            else:
                content.append(file.strip())
        return content

    def get_list(self,name):
        content=[]
        with open(name) as f:
            allfiles=f.readlines()
        for file in allfiles:
            content.append(file.strip())
        
        return content

    def _get_annotation(self,vertex_info, height, width):

        cx, cy, w, h = [float(i) for i in vertex_info]
        cx = cx * width
        cy = cy * height
        w = w * width
        h = h * height
        x = cx - w / 2
        y = cy - h / 2

        segmentation = [[x, y, x + w, y, x + w, y + h, x, y + h]]
        area = w * h

        bbox = [x, y, w, h]
        return segmentation, bbox, area
        
    def read_annotation(self,txtfile,img_id,height,width,annotation_id):
        annotation=[]

        if not Path(txtfile).exists():
            return {},0
        with open(txtfile) as f:
                allinfo=f.readlines()      

        for line in allinfo:
                label_info=line.replace('\n', '').replace('\r', '')
                label_info=label_info.strip().split(" ")
                if len(label_info) < 5:
                    continue

                category_id, vertex_info = label_info[0], label_info[1:]
               
                segmentation, bbox, area = self._get_annotation(vertex_info, height, width)
                annotation.append( {
                            'segmentation': segmentation,
                            'area': area,
                            'iscrowd': 0,
                            'image_id': img_id,
                            'bbox': bbox,
                            'category_id': str(int(category_id)+1),
                            'id': annotation_id,
                        })
                annotation_id+=1
              
        return annotation,annotation_id

    def get_category(self):

        for id,category in enumerate(self.name_lists,1):
          self.categories.append({
            'id': id,
            'name': category,
            'supercategory': category,
        } )

    def generate(self):
        self.classnum= self.getint("classes")
        self.train= Path( self.src_data).parent / Path(self.getstring("train")).name 
        self.valid= Path( self.src_data).parent / Path(self.getstring("valid")).name 
        self.names=Path( self.src_data).parent / Path(self.getstring("names")).name 
        self.train_files=self.get_path(self.train)
        self.valid_files=self.get_path(self.valid)
        self.name_lists=self.get_list(self.names)
        self.get_category()
        
        dest_path_train=Path(self.dst)/self.coco_train
        self.gen_dataset(self.train_files,dest_path_train,self.coco_train_json)

        dest_path_valid=Path(self.dst)/self.coco_valid
        
        self.gen_dataset(self.valid_files,dest_path_valid,self.coco_valid_json)

#  https://cocodataset.org/#format-data
    def gen_dataset(self,file_lists,target_img_path,target_json):
           
        images=[]
        annotations=[]
        annotation_id=1
        for img_id,file in   enumerate(file_lists,1):
            txt= str(Path(file).parent / Path(file).stem) + ".txt"  # from 0,  0 readhead, 1 stamp
            shutil.copyfile(file,target_img_path/ Path(file).name)
            imgsrc = cv.imread(file) # 读取图片
            image = imgsrc.shape #  获取图片宽高及通道数
            height = image[0]
            width = image[1]
            images.append({
                'date_captured': '2021',
                'file_name': str(Path(file).name),
                'id': img_id,
                           
                'height': height,
                'width': width,
            })

            if Path(txt).exists():
                new_anno,annotation_id=self.read_annotation(txt,img_id,height,width,annotation_id)
                if len(new_anno)>0:
                    annotations.extend(new_anno)
          


        json_data = {
            'info': self.info,
            'images': images,
            'licenses': self.licenses,
            'type': self.type,
            'annotations': annotations,
            'categories': self.categories,
        }
        with open(target_json, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False)

      


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Datasets converter from yolo to coco', add_help=False)

    parser.add_argument('--data_path', default='data/getn_config.data',
                        help='Dataset root path')
    parser.add_argument('--split', default='train2017',
                        help='Dataset split part, optional: [train2017, val2017]')

    args = parser.parse_args()

    converter = YOLO2COCO(args.data_path)
    converter.generate()
