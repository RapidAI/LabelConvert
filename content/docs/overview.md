---
weight: 40
date: "2023-09-08"
draft: false
author: "SWHL"
title: "Overview"
icon: "circle"
toc: true
description: ""
publishdate: "2023-09-08"
---


<div align="center">
  <img src="https://github.com/RapidAI/LabelConvert/releases/download/v0/LabelConvertv3.png" width="55%" height="55%"/>
</div>

## Label Convert

<p align="left">
    <a href=""><img src="https://img.shields.io/badge/Python->=3.6,<3.12-aff.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Win%2C%20Mac-pink.svg"></a>
    <a href="https://github.com/RapidAI/LabelConvert/graphs/contributors"><img src="https://img.shields.io/github/contributors/RapidAI/LabelConvert?color=9ea"></a>
    <a href="https://github.com/RapidAI/LabelConvert/stargazers"><img src="https://img.shields.io/github/stars/RapidAI/LabelConvert?color=ccf" ></a>
    <a href="https://pepy.tech/project/label_convert"><img src="https://static.pepy.tech/badge/label_convert?period=total&units=abbreviation&left_color=grey&right_color=blue&left_text=Downloads"></a>
    <a href="https://pypi.org/project/label_convert/"><img alt="PyPI" src="https://img.shields.io/pypi/v/label_convert"></a>
    <a href="https://choosealicense.com/licenses/apache-2.0/"><img src="https://img.shields.io/badge/License-Apache%202-dfd.svg"></a>
    <a href="https://semver.org/"><img alt="SemVer2.0" src="https://img.shields.io/badge/SemVer-2.0-brightgreen"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

A dataset format conversion tool for object detection and image segmentation, which supports mutual conversion between **labelme, labelImg tools and YOLO, VOC, and COCO** dataset formats.


### Supported conversions
```mermaid
flowchart LR

A(labelImg) --> B(YOLOv5)
A --> C(PubLayNet)
D(COCO) --> A
E(YOLOv5 YAML) --> D
F(darknet) --> D
```

### Installation
```bash {linenos=table}
pip install label_convert
```

### Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
