# Keras-CNN

## 概要
kerasのCNNを用いた二値分類問題を解く

## データセット
[Dogs vs. Cats](https://www.kaggle.com/c/dogs-vs-cats/data)　の画像データを使用する。

## 環境
Python 3.6.4 :: Anaconda, Inc.
keras  2.2.2

## ファイル/フォルダ構成
Keras-CNN
├── config.py
├── data
│   ├── test
│   │   ├── cats
│   │   │   ├── cat.*.jpg
│   │   │   .
│   │   │   .
│   │   │ 
│   │   └── dogs
│   │       ├── dog.*.jpg
│   │       .
│   │       .
│   │  
│   └── train
│       ├── cats
│       │   ├── cat.*.jpg
│       │   .
│       │   .
│       │ 
│       └── dogs
│           ├── dog.*.jpg
│           .
│           .
├── main.py
├── model.py
└── train.py
