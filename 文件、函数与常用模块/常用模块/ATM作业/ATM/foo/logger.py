import os,logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def record(message):
	logging.basicConfig(filename='%s/logger/record.log'%(BASE_DIR),format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)
	logging.debug(message)
def info(message,data):#info级别输出到文件以及屏幕
	ch = logging.StreamHandler()
	ch.setLevel(logging.INFO)
	fh = logging.FileHandler('%s/logger/%s.log'%(BASE_DIR,data['username']))
	fh.setLevel(logging.DEBUG)
	ch_formatter = logging.Formatter('%(message)s')
	fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
	ch.setFormatter(ch_formatter)
	fh.setFormatter(fh_formatter)
	logger = logging.getLogger("shopping")
	logger.handlers.clear()
	logger.setLevel(logging.INFO)
	logger.addHandler(ch)
	logger.addHandler(fh)
	logger.info(message)