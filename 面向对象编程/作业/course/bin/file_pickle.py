import os
import pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def read_file(file_name,mode='rb'):
	f = open('%s/pickle/%s.pickle'%(BASE_DIR,file_name),mode)
	data = pickle.load(f)
	f.close()
	return data

def write_file(data,file_name,mode='wb'):
	f = open('%s/pickle/%s.pickle'%(BASE_DIR,file_name),mode)
	pickle.dump(data,f)
	f.close()
