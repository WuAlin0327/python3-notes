import os
import sys
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from bin import server

def main():
	s = server.Server(('127.0.0.1',8082))
	s.run()

main()