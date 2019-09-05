class Person:

	'''人的类'''
	def __init__(self, name):
		self.name = name

	def an_zhuang_zidan(self)

class Gun:
	'''枪的类'''
	def __init__(self, name):
		self.name = name


class Bullet:
	'''弹夹类'''
	def __init__(self, max_num):
		self.max_num = max_num


class Zidan:
	def __init__(self, shang_hai):
		self.shang_hai = shang_hai


def main():
	"""用来控制整个程序的流程"""
	pass

	# 1. 创建老王对象
	laowang = Person('老王')
	# 2. 创建一个枪对象
	ak47 = Gun('AK47')
	# 3. 创建一个弹夹对象
	danjia = Bullet(100)
	# 4. 创建一些子弹
	zidan = Zidan(10)
	# 5. 创建一个敌人

	# 6. 老王把子弹安装到弹夹中
	laowang.an_zhuang

	# 7. 老王把弹夹安装到枪中

	# 8. 老王拿枪

	# 9. 老王开枪打敌人


if __name__ == '__main__':
	main()
