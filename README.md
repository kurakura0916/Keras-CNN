# Keras-CNN

## 概要
kerasのCNNを用いた二値分類問題を解く

## データセット
[Dogs vs. Cats](https://www.kaggle.com/c/dogs-vs-cats/data)　の画像データを使用する。

## 環境
Python 3.6.4 :: Anaconda, Inc.
keras  2.2.2

## ファイル/フォルダ構成

```
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
```

## 学習

```
python train.py
```

cats_and_dogs.h5の名前でモデルがディレクトリ内に保存されます。

## テスト
data/test　フォルダ内の画像1枚を使用しラベル（dog or cat）を予測する。

```
python main.py
```

以下のような形でdogである確率（predict score）が出力されます。
また同時にテスト画像のラベルと予測されたモデルも出力されます。
```
predict_score:0.9226323962211609
テストラベル:dog
予測ラベル:dogs
```

