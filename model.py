"""
モデルのネットワークを定義するためのモジュール。
"""
from keras import layers
from keras import models
import config as cf

def Mynet():
    model = models.Sequential()
    model.add(layers.Conv2D(32,(3,3),activation="relu",input_shape=(cf.img_height,cf.img_width,3))) #インプットサイズ(150×150)
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Conv2D(64,(3,3),activation="relu"))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Conv2D(128,(3,3),activation="relu"))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Conv2D(128,(3,3),activation="relu"))
    model.add(layers.Flatten()) # 平滑化を行う
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(512,activation="relu"))
    model.add(layers.Dense(1,activation="sigmoid"))

    return model