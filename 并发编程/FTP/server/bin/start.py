
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import server

def main():
	s = server.Server()
	s.monitor()


if __name__ == '__main__':
	main()