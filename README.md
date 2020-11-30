# pyxel_class_booker
BookerというPyxel(Python)向けのクラスを公開しています。  
Bookerクラスは、値の変化を予約できます。  

![pyxel-201201-001204](https://user-images.githubusercontent.com/32491347/100627345-3c879300-336a-11eb-81d0-bef3daa7578a.gif)

## 使い方
予約時はBooker.add()を使います。  
Booker.add(`対象インスタンス(obj)`, `の変数名(str)`, `変化させたい量(int)`, `変化開始時間(単位フレーム後開始)(int)`, `変化に要する時間(0<int)`, `イージング(str)`)  

イージングとは値の変わり方の種類のことで、本クラスではCubicなベジェ曲線を使用しています。(カスタマイズ可)  
イージングは`linear`(直線,デフォルト), `ease in`(加速), `ease out`(減速), `ease in out`(ふわっ)の4種類があります。  

出力時はBooker.do()を使います。  
1フレームで一度だけ実行してください。  
update()の後ろのほうに書くのがおすすめです。Booker.add()より前に書くとうまく実行されません。

## 配布 兼 サンプルコード
https://github.com/namosuke/pyxel_class_booker/blob/main/booker_example.py

## 使用時の注意
改変は自由ですが、配布元の記述は残しておいたほうが提出時に身のためになると思います。

## 使い方の例
10フレーム後に60フレーム使ってself.yに160加える
```py
Booker.add(self, 'y', 160, 10, 60)
```

0になっているself.flagをスペースキーが押された30フレーム後に1にする
```py
if pyxel.btnp(pyxel.KEY_SPACE):
  Booker.add(self, 'flag', 1, 30, 1)
```
