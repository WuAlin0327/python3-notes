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
		num = int(input('>>>').strip())
		func_str = func_l[num-1][1]
		if hasattr(Select,func_str):
			obj = Select()
			func = getattr(obj,func_str)
			func()


if __name__ == '__main__':
	main()