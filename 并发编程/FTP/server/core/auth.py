import os
import sys
import pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.user import User
class Auth:

	def laned(self,msg):

		with open('%s/conf/userinfo'%BASE_DIR,'r') as f1:
			for line in f1:
				print(line)
				username,password,user_dir = line.strip().split('|')
				if msg['username'] == username and msg['password'] == password:
					with open(r'%s'%user_dir,'rb') as f2:
						user_obj = pickle.load(f2)
						#登陆成功之后返回登陆状态和用户对象
						return {
							'status':True,
							'user_obj':user_obj,
							'username':username
						}
				else:
					return {'status':False}
			else:
				return {'status':False}



	def registered(self,msg):
		user_obj = User(msg['username'])
		with open('%s/conf/user_pickle/%s'%(BASE_DIR,user_obj.name),'wb') as f:#把用户对象保存为pickle文件
			pickle.dump(user_obj,f)
		with open('%s/conf/userinfo'%BASE_DIR,'a') as f:
			try:
				user_dir = '%s/home/%s'%(BASE_DIR,user_obj.name)
				os.mkdir(user_dir)
				l = [msg['username'],msg['password'],user_obj.file_pick]
				f.write('|'.join(l)+'\n')
				return {
					'status':True,
					'user_obj':user_obj
				}
			except FileExistsError:#不能创建同名字的文件夹
				print('该用户已存在')
				return {'status':False}

