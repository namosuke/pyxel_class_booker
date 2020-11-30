# pyxel_class_booker
BookerというPyxel(Python)向けのクラスを公開しています。

![pyxel-201201-001204](https://user-images.githubusercontent.com/32491347/100627345-3c879300-336a-11eb-81d0-bef3daa7578a.gif)

Bookerクラスは、値の変化を予約できます。  

予約時はBooker.add()を使います。  
Booker.add(`対象インスタンス(obj)`, `の変数名(str)`, `変化させたい量(int)`, `変化開始時間(単位フレーム後開始)(int)`, `変化に要する時間(0<int)`, `イージング(str)`)  

イージングとは値の変わり方の種類のことで、本クラスではCubicなベジェ曲線を使用しています。(カスタマイズ可)  
イージングは`linear`(直線,デフォルト), `ease in`(加速), `ease out`(減速), `ease in out`(ふわっ)の4種類があります。  

出力時はBooker.do()を使います。  
1フレームで一度だけ実行してください。
update()の後ろのほうに書くのがおすすめです。Booker.add()より前に書くとうまく実行されません。
