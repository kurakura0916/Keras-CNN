from model import Mynet
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
import config as cf

def train():
    model = Mynet()
    model.summary()

    print("train start!!")

    # モデルをコンパイル
    model.compile(loss="binary_crossentropy",
                  optimizer=optimizers.RMSprop(lr=1e-4),
                  metrics=["acc"])

    # データの水増しをしてジェネレーターを作成
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,# 回転
        width_shift_range=0.2,# 水平方向への移動
        height_shift_range=0.2,# 垂直方向への移動
        shear_range=0.2,# シアー変換
        zoom_range=0.2,
        horizontal_flip=True,# 水平方向へ反転
        fill_mode="nearest"
    )

    # 検証用データは水増ししない!
    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        cf.train_dir, # 訓練用画像のフォルダディレクトリ
        target_size=(150,150),
        batch_size=20,
        class_mode="binary"
    )

    validation_generator = test_datagen.flow_from_directory(
        cf.test_dir,
        target_size=(150,150),
        batch_size=20,
        class_mode="binary"
    )


    history = model.fit_generator(
        train_generator,
        steps_per_epoch=100,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=50
    )

    model.save(cf.model_path)

    print("train end!!")

if __name__ == '__main__':
    train()