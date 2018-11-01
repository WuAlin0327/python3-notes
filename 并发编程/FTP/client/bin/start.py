import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.auth import Select

def main():
	func_l = [
		('登陆','laned'),
		('注册','registered'),
		('退出','exit')
	]
	for index,item in enumerate(func_l,1):
		print(index,item[0])
	while True:
		num = input('请选择：').strip()
		if not num.isdigit() or int(num)>3:
			print('请输入正确序号选择操作')
			continue
		func_str = func_l[int(num)-1][1]
		print(func_str)
		if hasattr(Select,func_str):
			obj = Select()#建立与服务端的链接，并继承了Trans类
			func1 = getattr(obj,func_str)
			ret = func1()
			if ret['status']:
				while True:
					in_cmd = input('>>>').strip()
					cmd,filename = in_cmd.split()
					if hasattr(obj,cmd):
						func2 = getattr(obj,cmd)
						func2(cmd,filename)
			else:
				print('登陆失败')
				continue

		else:
			print('没有该方法')
if __name__ == '__main__':
	main()