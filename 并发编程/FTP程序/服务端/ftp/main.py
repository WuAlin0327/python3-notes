import os
import sys
from concurrent.futures import ThreadPoolExecutor
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from bin import server

def main():
	s = server.Server(('127.0.0.1',8189))
	s.run()

if __name__ == '__main__':
	main()