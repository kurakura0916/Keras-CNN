"""
各種設定用のパラメータ
"""
import  os
from keras.preprocessing import image

# モデルのインプットサイズ
img_height = 150
img_width = 150

# dataフォルダのディレクトリ
base_dir = "/Users/hiroki.kurasawa/Documents/Keras-CNN/data"
# 訓練用のフォルダディレクトリ
train_dir = os.path.join(base_dir,"train")
# 訓練用猫画像のフォルダディレクイ
train_cats_dir = os.path.join(train_dir,"cats")
# 訓練用犬画像のフォルダディレクイ
train_dogs_dir = os.path.join(train_dir,"dogs")

# テスト用のフォルダディレクトリ
test_dir = os.path.join(base_dir,"test")
# テスト用猫画像のフォルダディレクトリ
test_cats_dir = os.path.join(test_dir,"cats")
# テスト用犬画像のフォルダディレクトリ
test_dogs_dir = os.path.join(test_dir,"dogs")

model_path = "cats_and_dogs.h5"

# テスト用の画像ファイル
test_img_cats = os.path.join(test_cats_dir,"cat.1500.jpg")
test_img_dogs = os.path.join(test_dogs_dir,"dog.1935.jpg")
