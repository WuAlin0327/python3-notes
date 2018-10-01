'''
hasattr(obj,'name')# 判断对象有没有'name'属性 obj.__dict__['name']

getattr(obj,'name') # 拿到对象的属性

setattr(obj,'name','wualin')#修改 obj.name = 'wualin'

delattr(obj,'age')# del obj.age
以上方法同样适用于类
'''
# 反射的应用：
class Service:
	def run(self):
		while True:
			cmd = input('>>>:').strip()
			if hasattr(self,cmd):
				func = getattr(self,cmd)
				func()
	def get(self):
		print('get...')

	def put(self):
		print('put...')
obj = Service()
obj.run()
