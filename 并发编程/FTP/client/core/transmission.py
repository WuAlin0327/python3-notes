class Trans:
	'''
	数据传输：
		get filename: 下载
		put filename: 上传
		ls /: 查看用户目录下的文件以及文件大小
		cd folder:	切换工作目录
	'''
	def get(self,cmd,filename):
		print(cmd,filename)

	def put(self,cmd,filename):
		print(cmd,filename)

	def ls(self,cmd,filename):
		pass

	def cd(self,cmd,filename):
		pass