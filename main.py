import numpy as np
from keras.preprocessing.image import load_img,img_to_array
import config as cf
import model

def main():
    labels = ["cats","dogs"]

    Mymodel = model.Mynet()
    Mymodel.load_weights(cf.model_path)
    Mymodel.summary()

    #img = load_img(cf.test_img_cats,target_size=(cf.img_height,cf.img_width))
    img = load_img(cf.test_img_dogs, target_size=(cf.img_height, cf.img_width))
    img = img_to_array(img)

    img = img.astype("float32")/255
    img = np.array([img]) # 4次元配列に変換

    y_pred = Mymodel.predict(img)
    print("predict_score:{}".format(y_pred[0][0]))
    y_pred = np.round(y_pred)
    y_pred = np.int(y_pred)

    #print("テストラベル:cats")
    print("テストラベル:dog")
    print("予測ラベル:{}".format(labels[y_pred]))

if __name__ == "__main__":
    main()
