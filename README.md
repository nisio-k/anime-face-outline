# アニメ画像の顔＆線画抽出

アニメ画像を渡すと顔周りの線画を抽出し、機械学習用の画像を出力します。
顔認識には[lbpcascade_animeface.xml](https://github.com/nagadomi/lbpcascade_animeface)を使用しています。


## 出力される画像

![]()

こんな感じで線画と元画像が並びます。
元の画像は[イラストAC](https://www.ac-illust.com/main/detail.php?id=648361&word=%E3%81%8A%E8%8F%93%E5%AD%90%E3%81%AE%E5%B0%91%E5%A5%B3)からお借りしました。

## ディレクトリ構成

```
root
 ├ lbpcascade_animeface.xml
 ├ noresize	-- リサイズできなかった画像が入ります
 ├ origin	-- 参照先
 ├ output	-- 出力先
 └ senga.py
```

## 参考

* [カラー画像から線画を作る[OpenCV & python] - MATHGRAM](https://www.mathgram.xyz/entry/cv/contour)
* [nagadomi/lbpcascade_animeface: A Face detector for anime/manga using OpenCV](https://github.com/nagadomi/lbpcascade_animeface)