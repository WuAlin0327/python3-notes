import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def storage(args):
	size = 0
	file = os.listdir('%s/warehouse/%s/'%(BASE_DIR,args))
	for i in file:
		file_size = os.path.getsize('%s/warehouse/%s/%s'%(BASE_DIR,args,i))
		size+=file_size
	return size



