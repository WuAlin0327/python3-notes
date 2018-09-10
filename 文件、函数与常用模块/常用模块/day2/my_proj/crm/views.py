import sys,os
from proj import settings
BEAS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #os.path.abcpath()获取当前文件的绝对路径
sys.path.append(BEAS_DIR)


def sayhi():
	print("in crm/wiews")

settings.sayhello()
