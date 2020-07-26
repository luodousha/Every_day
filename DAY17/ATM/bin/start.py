import sys
import os
# print(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core.src import run

	
if __name__ == '__main__':
	while True:
		run()		