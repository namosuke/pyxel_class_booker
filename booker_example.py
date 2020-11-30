import pyxel

# Bookerクラス：値の変化を予約する
# イベント登録時：update()内でBooker.add()を使う
# Booker.add(対象インスタンス(obj), の変数名(str), 変化させたい量(int),
#   変化開始時間(単位フレーム後開始)(int), 変化に要する時間(0<int), イージング(str))
# イージングはCubicなベジェ曲線を使用(カスタマイズ可)、デフォルトは'linear'
# イベント出力時：Booker.do()をBooker.add()より後ろに記述し、毎フレーム実行する
# 配布元：https://github.com/namosuke/pyxel_class_booker
class Booker:
	books = []
	fr = 0
	
	@classmethod
	def add(cls, obj, key, value, start_time, end_time, easing = 'linear'):
		cls.books.append([
			cls.fr + start_time,
			end_time,
			key,
			value,
			0,  # 最後の差分
			easing,
			obj
		])
	
	@classmethod
	def do(cls):
		# 逆順にアクセス
		for i in range(len(cls.books) - 1, -1, -1):
			b = cls.books[i]  # 予約情報
			if b[0] <= cls.fr:
				# イージング処理参考　http://nakamura001.hatenablog.com/entry/20111117/1321539246
				if b[5] == 'linear':
					diff = b[3] * (cls.fr - b[0]) / b[1]
				elif b[5] == 'ease in':
					t = (cls.fr - b[0]) / b[1]
					diff = b[3] * t*t*t
				elif b[5] == 'ease out':
					t = (cls.fr - b[0]) / b[1]
					t -= 1
					diff = b[3] * (t*t*t + 1)
				elif b[5] == 'ease in out':
					t = (cls.fr - b[0]) / (b[1] / 2)
					if t < 1:
						diff = (b[3] / 2) * t*t*t
					else:
						t -= 2
						diff = (b[3] / 2) * (t*t*t + 2)

				# 小数誤差を無くすため、毎回整数値を反映させている
				b[6].__dict__[b[2]] -= b[4]
				b[6].__dict__[b[2]] += round(diff)
				b[4] = round(diff)

			if b[0] + b[1] <= cls.fr:
				del cls.books[i]
				
		cls.fr += 1

class App:
	def __init__(self):
		pyxel.init(200, 160)
		pyxel.mouse(True)
		self.flag = 1
		self.x = self.y = 300
		pyxel.run(self.update, self.draw)
	
	def update(self):
		if self.flag:
			self.flag = 0
			Booker.add(self, 'flag', 1, 80, 1)
			self.ball1 = self.ball2 = self.ball3 = self.ball4 = 20
			Booker.add(self, 'ball1', 160, 10, 60)
			Booker.add(self, 'ball2', 160, 10, 60, 'ease in')
			Booker.add(self, 'ball3', 160, 10, 60, 'ease out')
			Booker.add(self, 'ball4', 160, 10, 60, 'ease in out')
		self.x = self.y = 0
		Booker.add(self, 'x', pyxel.mouse_x, 5, 1)
		Booker.add(self, 'y', pyxel.mouse_y, 5, 1)
		Booker.do()
	
	def draw(self):
		pyxel.cls(7)
		pyxel.text(10, 10, 'linear:      ' + str(self.ball1), 0)
		pyxel.circ(self.ball1, 25, 7, 8)
		pyxel.text(10, 40, 'ease in:     ' + str(self.ball2), 0)
		pyxel.circ(self.ball2, 55, 7, 6)
		pyxel.text(10, 70, 'ease out:    ' + str(self.ball3), 0)
		pyxel.circ(self.ball3, 85, 7, 10)
		pyxel.text(10, 100, 'ease in out: ' + str(self.ball4), 0)
		pyxel.circ(self.ball4, 115, 7, 11)
		pyxel.circ(self.x, self.y, 4, 14)

App()