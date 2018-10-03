import os,sys
import pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from bin import Studen as s
# from . import landing
def main():
	print('''
	1. 学员
	2. 讲师
	3. 管理员
	''')
	while True:
		sum = input('请选择身份：')
		if sum == '1':
			print('''
	1. 注册
	2. 登陆
			''')
			num = input('请选择注册 or 登陆:')
			if num == '1':
				data = {}
				username = input('username:')
				password = input('password:')
				data['username'] = username
				data['password'] = password
				data['status'] = 0
				f = open('%s/pickle/%s.pickle'%(BASE_DIR,username),'wb')
				pickle.dump(data,f)
			elif num == '2':
				username = input('username:')
				password = input('password:')
				f = open('%s/pickle/%s.pickle'%(BASE_DIR,username),'rb')
				data = pickle.load(f)
				if username == data['username'] and password == data['password']:
					pass


main()