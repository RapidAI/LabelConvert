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

## Introduction

A tool for object detection and image segmentation dataset format conversion.

Supports conversion between labelme tool annotated data, labelImg tool annotated data, YOLO, PubLayNet and COCO data set formats.

## Supported conversions

```mermaid
flowchart LR

A(YOLOv5) --> B(COCO)
C(YOLOv5 YMAL) --> B
D(darknet) --> B
E(labelme) --> B

B --> F(labelImg)
F --> G(PubLayNet)
F --> J(YOLOv5)

J --> H(YOLOv8)
H --> J
```

## Installation

```bash
pip install label_convert
```

## Documentation

Full documentation can be found on [docs](https://rapidai.github.io/LabelConvert/docs) in Chinese.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)
