---
weight: 40
date: "2023-09-08"
draft: false
author: "SWHL"
title: "概览"
icon: "circle"
toc: true
description: ""
publishdate: "2023-09-08"
---

<div align="center">
  <div align="center">
    <img src="https://github.com/RapidAI/LabelConvert/releases/download/v0/LabelConvertv3.png" width="55%" height="55%"/>
  </div>
  <br/>

  <a href=""><img src="https://img.shields.io/badge/Python->=3.6,<3.12-aff.svg"></a>
  <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Win%2C%20Mac-pink.svg"></a>
  <a href="https://github.com/RapidAI/LabelConvert/graphs/contributors"><img src="https://img.shields.io/github/contributors/RapidAI/LabelConvert?color=9ea"></a>
  <a href="https://github.com/RapidAI/LabelConvert/stargazers"><img src="https://img.shields.io/github/stars/RapidAI/LabelConvert?color=ccf" ></a>
  <a href="https://pepy.tech/project/label_convert"><img src="https://static.pepy.tech/badge/label_convert?period=total&units=abbreviation&left_color=grey&right_color=blue&left_text=Downloads"></a>
  <a href="https://pypi.org/project/label_convert/"><img alt="PyPI" src="https://img.shields.io/pypi/v/label_convert"></a>
  <a href="https://choosealicense.com/licenses/apache-2.0/"><img src="https://img.shields.io/badge/License-Apache%202-dfd.svg"></a>
  <a href="https://semver.org/"><img alt="SemVer2.0" src="https://img.shields.io/badge/SemVer-2.0-brightgreen"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

</div>

目标检测和图像分割的数据集格式转换工具，支持**labelme、labelImg与YOLO、VOC和COCO** 数据集格式之间的相互转换。


### 支持的转换
```mermaid
flowchart LR

A(YOLOv5) --> B(COCO)
C(YOLOv5 YMAL) --> B
D(darknet) --> B
E(labelme) --> B

B --> F(labelImg)
F --> G(PubLayNet)
F --> J(YOLOv5)
```

### 安装
```bash {linenos=table}
pip install label_convert
```

