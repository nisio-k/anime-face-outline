import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import glob
import os
import random
import shutil

classifier = cv2.CascadeClassifier("./lbpcascade_animeface.xml")

# オリジナル画像ディレクトリ
dir_origin = "./origin/"
# 出力用ディレクトリ
dir_out = "./output/"
# リサイズできなかった画像が出力されるディレクトリ
dir_noresize = "./noresize/"

img_origin = glob.glob("./origin/*")
img_length = len(img_origin)
img_size = 200

list_dir_origin = os.listdir(dir_origin)

# .DS_Storeを取り除く
if ".DS_Store" in list_dir_origin:
  index = list_dir_origin.index(".DS_Store")
  list_dir_origin.pop(index)

for num in range(img_length):
  src = str(img_origin[num])
  img = cv2.imread(img_origin[num])
  if img is None:
    print("Not Image :" + src)
    continue;
  else:
    img_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces =  classifier.detectMultiScale(img_gs, scaleFactor=1.1, minNeighbors=2, minSize=(img_size, img_size))
    # 顔がない場合
    if len(faces) == 0:
      print("no faces :" + src)
      continue
    # 複数の顔がある場合
    elif len(faces) > 1:
      print("not resized :" + src)
      shutil.copyfile(dir_origin + str(list_dir_origin[num]), dir_noresize + str(list_dir_origin[num]))
      continue
    # 顔が1つの時は処理をする
    else:
      # 顔の周りで切り抜く
      rect = faces[0]
      img = img[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
      img_gs = img_gs[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
      img_gbgr = cv2.cvtColor(img_gs, cv2.COLOR_GRAY2BGR)

      # 線画抽出
      neiborhood24 = np.array([[1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1]],
                               np.uint8)
      img_dilation = cv2.dilate(img_gbgr, neiborhood24, iterations=1)
      img_diff = cv2.absdiff(img_dilation, img_gbgr)
      img_contour = 255 - img_diff

      # リサイズしてカラーと線画を繋げる
      resize_color = cv2.resize(img, (img_size, img_size))
      resize_senga = cv2.resize(img_contour, (img_size, img_size))
      img_output = cv2.hconcat([resize_senga, resize_color])

      file_name = os.path.join(dir_out, str(list_dir_origin[num]) + ".jpg")
      cv2.imwrite(str(file_name), img_output)
