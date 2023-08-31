---
layout: home
title:
permalink: /
mermaid: true
---


<div align="center">
  <img src="https://github.com/RapidAI/YOLO2COCO/releases/download/v0/LabelConvertv3.png" width="55%" height="55%"/>
</div>

<br/>

<p align="left">
    <a href=""><img src="https://img.shields.io/badge/Python->=3.6,<3.12-aff.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Win%2C%20Mac-pink.svg"></a>
    <a href="https://github.com/RapidAI/YOLO2COCO/graphs/contributors"><img src="https://img.shields.io/github/contributors/RapidAI/YOLO2COCO?color=9ea"></a>
    <a href="https://github.com/RapidAI/YOLO2COCO/stargazers"><img src="https://img.shields.io/github/stars/RapidAI/YOLO2COCO?color=ccf" ></a>
    <a href="https://pepy.tech/project/label_convert"><img src="https://static.pepy.tech/personalized-badge/label_convert?period=total&units=abbreviation&left_color=grey&right_color=blue&left_text=Downloads"></a>
    <a href="https://pypi.org/project/label_convert/"><img alt="PyPI" src="https://img.shields.io/pypi/v/label_convert"></a>
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202-dfd.svg"></a>
    <a href="https://semver.org/"><img alt="SemVer2.0" src="https://img.shields.io/badge/SemVer-2.0-brightgreen"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

A dataset format conversion tool for object detection and image segmentation, which supports mutual conversion between **labelme, labelImg tools and YOLO, VOC, and COCO** dataset formats.


## Installation
```bash
pip install label_convert
```

```mermaid
flowchart LR

A([Documents]) --ExtractText--> B([sentences])
B --Embeddings--> C([Embeddings])
C --Store--> D[(DataBase)]
```

$$
\begin{align*}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{align*}
$$


$$
x^2 + y^2 = 1
$$