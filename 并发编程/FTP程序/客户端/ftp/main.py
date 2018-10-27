import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from bin import client

def main():
	c = client.Client(('127.0.0.1',8189))
	c.run()

main()