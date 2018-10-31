import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class User:
	'''
	保存用户信息的pickle文件
	保存内容：
		姓名
		磁盘大小
		文件总大小
		home目录

	'''

	def __init__(self,name):
		self.name = name
		self.disk = 1024*1024*2
		self.home = os.path.join('%s/home'%BASE_DIR,self.name)#保存用户上传文件的目录
		self.filesize = 0
		self.file_pick = '%s/conf/user_pickle/%s'%(BASE_DIR,self.name)#用户对象保存文件路径

	def upload(self):
		pass

	def download(self):
		pass